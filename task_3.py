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

def find_shortest_paths_dijkstra(graph, start_node):
    # Знаходимо довжини найкоротших шляхів від start_node до всіх інших
    lengths = nx.single_source_dijkstra_path_length(graph, source=start_node, weight='weight')
    # Знаходимо самі маршрути
    paths = nx.single_source_dijkstra_path(graph, source=start_node, weight='weight')
    
    return lengths, paths

# Виведення результатів

# Детальний маршрут для тестових точок
start = "Північний"
end = "Водолій"

print(f"\n--- Найшвидший маршрут (Дейкстра) від '{start}' до '{end}' ---")
shortest_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
travel_time = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')

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

    if len(path_str) > 50: path_str = path_str[:47] + "..."
    
    print(f"{station:<25} | {time:<10} | {path_str}")

if __name__ == "__main__":
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
