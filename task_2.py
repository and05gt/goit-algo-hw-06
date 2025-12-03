import networkx as nx
from collections import deque
from task_1 import G

# Алгоритм DFS (Пошук у глибину)
def dfs_iterative(graph, start_vertex, target_vertex):
    visited = set()
    stack = [(start_vertex, [start_vertex])]

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == target_vertex:
                return path
            visited.add(vertex)

            neighbors = list(graph[vertex])
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# Алгоритм BFS (Пошук у ширину)
def bfs_iterative(graph, start_vertex, target_vertex):
    visited = set()
    queue = deque([(start_vertex, [start_vertex])])

    while queue:
        (vertex, path) = queue.popleft()

        if vertex not in visited:
            if vertex == target_vertex:
                return path
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None
    
def find_paths(graph, start, end):
    print(f"\n--- Шукаємо шлях від '{start}' до '{end}' ---\n")

    dfs_path = dfs_iterative(graph, start, end)
    
    print(f"DFS (Пошук у глибину):")
    if dfs_path:
        print(f" -> Шлях: {dfs_path}")
        print(f" -> Кількість зупинок: {len(dfs_path) - 1}")
    else:
        print("DFS: Шлях не знайдено")
    
    print("-" * 30)

    bfs_path = bfs_iterative(graph, start, end)
    
    print(f"BFS (Пошук у ширину):")
    if bfs_path:
        print(f" -> Шлях: {bfs_path}")
        print(f" -> Кількість зупинок: {len(bfs_path) - 1}")
    else:
        print("BFS: Шлях не знайдено")
    
    return dfs_path, bfs_path

if __name__ == "__main__":
    start_station = "Північний"
    end_station = "Водолій"

    dfs_result, bfs_result = find_paths(G, start_station, end_station)

    print("\n--- Порівняння ---")
    if dfs_result and bfs_result:
        if len(dfs_result) == len(bfs_result):
            print("Алгоритми знайшли шляхи однакової довжини.")
        else:
            diff = len(dfs_result) - len(bfs_result)
            print(f"BFS знайшов коротший шлях на {diff} перегони(ів).")
            print("Це доводить, що BFS є оптимальним для пошуку найкоротшого шляху в незважених графах.")
        