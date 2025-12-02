import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Визначаємо лінії метро м. Миколаєва

# 1. Червона лінія: Від Намиву через весь проспект Центральний
red_line = [
    "Намив", "Ліски", "Центральний ринок", "Соборна",
    "Садова", "3-тя Слобідська", "Зоопарк", "Автовокзал"
]

# 2. Синя лінія: Від мікрорайону Північний через центр до Яхт-клубу
blue_line = [
    "Північний", "Соляні", "Парк Перемоги", "Адміральська",
    "Соборна", "Сухий Фонтан", "Яхт-клуб"
]

# 3. Зелена лінія: Від Центрального стадіону, перетинаючи інші лінії
green_line = [
    "Центральний стадіон", "Парк Перемоги", "6-та слобідська",
    "Зоопарк", "Залізничний вокзал", "Таврія", "Водолій"
]

def add_line(graph, stations, color):
    for station in stations:
        graph.add_node(station, color=color)
    for i in range(len(stations) - 1):
        graph.add_edge(stations[i], stations[i+1])

add_line(G, red_line, 'red')
add_line(G, blue_line, 'blue')
add_line(G, green_line, 'green')

transfer_stations = ["Соборна", "Зоопарк", "Парк Перемоги"]
for station in transfer_stations:
    G.nodes[station]['color'] = 'yellow' # Робимо пересадки жовтими

if __name__ == "__main__":
    # Візуалізація
    plt.figure(figsize=(16, 12))

    pos = nx.spring_layout(G, seed=42)

    colors = [G.nodes[n]['color'] for n in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=500)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    plt.title("Схема гіпотетичного метро м. Миколаїв", fontsize=16)
    plt.axis("off")
    plt.show()

    # Аналіз
    print("--- Аналіз Миколаївського метрополітену ---")
    print(f"Всього станцій: {G.number_of_nodes()}")
    print(f"Всього перегонів: {G.number_of_edges()}")

    # Сортуємо станції за важливістю (ступенем)
    degrees = sorted(G.degree, key=lambda x: x[1], reverse=True)
    print("\nТОП-3 найважливіших станцій (Хаби):")
    for node, degree in degrees[:3]:
        print(f"- Станція '{node}': {degree} з'єднань")
