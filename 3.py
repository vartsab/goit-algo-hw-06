import networkx as nx

# Ініціалізація графа
G = nx.Graph()

stations_R = [
    "Forest Hills - 71 Av", 
    "67 Av", 
    "63 Dr - Rego Park", 
    "Woodhaven Blvd",
    "Grand Av - Newtown", 
    "Elmhurst Av", 
    "Jackson Hts - Roosevelt Av", 
    "65 St",
    "Northern Blvd", 
    "46 St", 
    "Steinway St", 
    "36 St", 
    "Queens Plaza", 
    "Lexington Av/59 St", 
    "5 Av/59 St", 
    "57 St - 7 Av", 
    "49 St", 
    "Times Sq - 42 St",
    "34 St - Herald Sq", 
    "28 St", 
    "23 St", 
    "14 St - Union Sq", 
    "8 St - NYU",
    "Prince St", 
    "Canal St", 
    "City Hall", 
    "Cortlandt St", 
    "Rector St",
    "Whitehall St - South Ferry", 
    "Court St", 
    "Jay St - MetroTech", 
    "DeKalb Av", 
    "Atlantic Av - Barclays Ctr", 
    "Union St", 
    "9 St", 
    "Prospect Av",
    "25 St", 
    "36 St", 
    "45 St", 
    "53 St", 
    "59 St", 
    "Bay Ridge Av", 
    "77 St",
    "86 St", 
    "Bay Ridge - 95 St"
]

stations_N = [
    "Astoria - Ditmars Blvd", 
    "Astoria Blvd", 
    "30 Av", 
    "Broadway",
    "36 Av", 
    "39 Av - Dutch Kills", 
    "Queensboro Plaza", 
    "Lexington Av/59 St",
    "5 Av/59 St", 
    "57 St - 7 Av", 
    "49 St", 
    "Times Sq - 42 St",
    "34 St - Herald Sq", 
    "28 St", 
    "23 St", 
    "14 St - Union Sq", 
    "8 St - NYU",
    "Prince St", 
    "Canal St", 
    "City Hall", 
    "Cortlandt St", 
    "Rector St",
    "Whitehall St - South Ferry", 
    "Court St", 
    "Jay St - MetroTech", 
    "DeKalb Av", 
    "Atlantic Av - Barclays Ctr", 
    "36 St", 
    "45 St", 
    "53 St",
    "59 St", 
    "8 Av", 
    "Fort Hamilton Pkwy", 
    "New Utrecht Av", 
    "18 Av", 
    "20 Av", 
    "Bay Pkwy", 
    "Kings Hwy", 
    "Avenue U", 
    "86 St", 
    "Coney Island - Stillwell Av"
]

stations_D = [
    "Norwood - 205 St", 
    "Bedford Park Blvd", 
    "Kingsbridge Rd", 
    "Fordham Rd",
    "182-183 Sts", 
    "Tremont Av", 
    "174-175 Sts", 
    "170 St", 
    "167 St", 
    "161 St - Yankee Stadium",
    "155 St", 
    "145 St", 
    "7 Av", 
    "47-50 Sts - Rockefeller Ctr", 
    "42 St - Bryant Pk",
    "34 St - Herald Sq", 
    "23 St", 
    "14 St", 
    "W 4 St - Washington Sq", 
    "Broadway-Lafayette St",
    "Grand St", 
    "Atlantic Av - Barclays Ctr", 
    "36 St", 
    "9 Av", 
    "Fort Hamilton Pkwy", 
    "50 St", 
    "55 St", 
    "62 St", 
    "71 St", 
    "79 St", 
    "18 Av", 
    "20 Av", 
    "Bay Pkwy", 
    "25 Av", 
    "Bay 50 St", 
    "Coney Island - Stillwell Av"
]


# Задамо умовну відстань між станціями
distances_R = [1, 1.2, 1.5, 2, 1.8, 1, 1.1, 0.9, 1.3, 1.2, 1.4, 1.7, 1.5, 1.1, 0.8, 1.2, 0.7, 0.9, 0.9, 1.2, 0.8, 1, 1.1, 0.9, 0.7, 0.6, 0.8, 1.4, 1.2, 1.6, 1.3, 1.1, 1.4, 1.3, 1.2, 1, 1.2, 0.9, 1.1, 1.1, 0.8, 0.9, 1, 0.85]
distances_N = [1.1, 1.2, 1.3, 1.4, 1.5, 1.2, 1.3, 1.1, 0.8, 1.2, 0.7, 0.9, 0.9, 1.2, 0.8, 1, 1.1, 0.9, 0.7, 0.6, 0.8, 1.4, 1.2, 1.6, 1.3, 1.1, 1.4, 1.3, 1.2, 1, 1.2, 0.9, 1.1, 1.1, 0.8, 0.9, 1.2, 1.4, 1.6, 1.2]
distances_D = [1.3, 1.4, 1.2, 1.6, 1.1, 1.3, 1.5, 1.4, 1.2, 1.3, 1.1, 1.4, 1.3, 1.2, 1.5, 1.1, 1.4, 1.3, 1.1, 1.5, 1.4, 1.2, 1.3, 1.2, 1.3, 1.4, 1.2, 1.5, 1.3, 1.2, 1.4, 1.3, 1.5, 1.4, 1.1]


# Додамо станції та відстань між ними до графа
for stops, distances in [(stations_R, distances_R), (stations_N, distances_N), (stations_D, distances_D)]:
    if len(stops) - 1 != len(distances):
        raise ValueError("The number of distances must match the number of connections (stations - 1).")
    for i in range(len(stops) - 1):
        G.add_edge(stops[i], stops[i + 1], weight=distances[i], line='R' if stops == stations_R else 'N' if stops == stations_N else 'D')

# Функція для алгоритму Дейкстри без використання сторонніх бібліотек
def dijkstra(graph, start, goal):
    # Ініціалізація відстаней
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes}
    unvisited = list(graph.nodes)
    
    while unvisited:
        # Вибір вузла з найменшою відстанню
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)
        
        if distances[current_node] == float('inf'):
            break
        
        # Оновлення відстаней до сусідніх вузлів
        for neighbor, attrs in graph[current_node].items():
            weight = attrs.get('weight', 1)
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                
        if current_node == goal:
            break

    # Відновлення шляху
    path, current = [], goal
    while previous_nodes[current] is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    if path:
        path.insert(0, current)
    
    return path, distances[goal]

# Пошук найкоротшого шляху між всіма вершинами
all_shortest_paths_custom = {}
for source in G.nodes():
    all_shortest_paths_custom[source] = {}
    for target in G.nodes():
        if source != target:
            path, length = dijkstra(G, source, target)
            all_shortest_paths_custom[source][target] = (path, length)

# Виведення прикладу результатів
start_station = "Forest Hills - 71 Av"
goal_station = "Coney Island - Stillwell Av"

shortest_path_custom, path_length_custom = dijkstra(G, start_station, goal_station)
print(f"Shortest path from {start_station} to {goal_station}: {shortest_path_custom} with total length: {path_length_custom}")

# Аналіз результатів
num_paths_custom = sum(len(paths) for paths in all_shortest_paths_custom.values())
print(f"Total number of shortest paths calculated: {num_paths_custom}")