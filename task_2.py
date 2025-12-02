import networkx as nx
from task_1 import G

def find_paths(graph, start, end):
    print(f"\n--- Шукаємо шлях від '{start}' до '{end}' ---\n")

    # 1. Алгоритм DFS
    t_dfs = nx.dfs_tree(graph, source=start)
    try:
        dfs_path = nx.shortest_path(t_dfs, source=start, target=end)
        print(f"DFS (Пошук у глибину):")
        print(f" -> Шлях: {dfs_path}")
        print(f" -> Кількість зупинок: {len(dfs_path) - 1}")
    except nx.NetworkXNoPath:
        dfs_path = []
        print("DFS: Шлях не знайдено")
    
    print("-" * 30)

    # 2. Алгоритм BFS
    try:
        bfs_path = nx.shortest_path(graph, source=start, target=end)
        print(f"BFS (Пошук у ширину / Найкоротший шлях):")
        print(f" -> Шлях: {bfs_path}")
        print(f" -> Кількість зупинок: {len(bfs_path) - 1}")
    except nx.NetworkXNoPath:
        bfs_path = []
        print("BFS: Шлях не знайдено")
    
    return dfs_path, bfs_path

if __name__ == "__main__":
    start_station = "Північний"
    end_station = "Водолій"

    dfs_result, bfs_result = find_paths(G, start_station, end_station)

    print("\n--- Порівняння ---")
    if len(dfs_result) == len(bfs_result):
        print("Алгоритми знайшли шляхи однакової довжини.")
    else:
        print(f"BFS знайшов коротший шлях на {len(dfs_result) - len(bfs_result)} перегони(ів).")
        