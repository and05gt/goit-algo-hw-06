import networkx as nx
import matplotlib.pyplot as plt
from task_1 import G

# Стандартний час всім перегонам - 2 хвилини
for u, v in G.edges():
    G[u][v]['weight'] = 2

# Час для складних ділянок (мости, довгі відстані)
G["Парк Перемоги"]["Адміральська"]['weight'] = 5
G["Північний"]["Соляні"]['weight'] = 3
G["Залізничний вокзал"]["Таврія"]['weight'] = 5
G["Таврія"]["Водолій"]['weight'] = 6
G["Зоопарк"]["Залізничний вокзал"]['weight'] = 3

def dijkstra_algorithm(graph, start):
    """Returns a dictionary of distances and a dictionary of predecessors for path reconstruction."""

    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    previous_nodes = {vertex: None for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor].get('weight', 1)
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    """Auxiliary function: restores the list of stations from start to finish"""

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        if current_node == start:
            break
        current_node = previous_nodes[current_node]
    
    if path[-1] != start and start != end:
        return []
        
    return path[::-1]

def find_shortest_paths_dijkstra(graph, start_node):
    """Wrapper: returns (lengths, paths) for all nodes."""

    distances, previous_nodes = dijkstra_algorithm(graph, start_node)
    
    paths = {}
    for node in graph.nodes():
        paths[node] = reconstruct_path(previous_nodes, start_node, node)
        
    return distances, paths

if __name__ == "__main__":
    # Детальний маршрут для тестових точок
    start = "Північний"
    end = "Водолій"

    print(f"\n--- Найшвидший маршрут (Дейкстра) від '{start}' до '{end}' ---")
    
    all_dists, all_paths = find_shortest_paths_dijkstra(G, start)
    shortest_path = all_paths[end]
    travel_time = all_dists[end]

    print(f"Маршрут: {shortest_path}")
    print(f"Загальний час: {travel_time} хв")

    print("-" * 40)

    # Знаходження найкоротших шляхів між всіма вершинами
    print("\n--- Розрахунок часу від 'Залізничний вокзал' до інших станцій ---")

    source_station = "Залізничний вокзал"
    lengths, paths = find_shortest_paths_dijkstra(G, source_station)

    # Сортуємо станції за часом доїзду
    sorted_destinations = sorted(lengths.items(), key=lambda item: item[1])

    print(f"{'Станція призначення':<25} | {'Час (хв)':<10} | {'Шлях'}")
    print("-" * 60)
    for station, time in sorted_destinations:
        if station == source_station:
            continue
        path_str = " -> ".join(paths[station])

        if len(path_str) > 50:
            path_str = path_str[:47] + "..."
        print(f"{station:<25} | {time:<10} | {path_str}")

    # Візуалізація з вагами
    plt.figure(figsize=(16, 12))

    pos = nx.spring_layout(G, seed=42)
    
    colors = [G.nodes[n]['color'] for n in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=500)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title("Метро м. Миколаєва з часом проїзду (вага ребер)", fontsize=16)
    plt.axis("off")
    plt.show()
