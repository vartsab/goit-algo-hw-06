import networkx as nx
from collections import deque

# Створення графа
G = nx.Graph()

# Додавання станцій та ліній
stations_R = [
    "Forest Hills - 71 Av", "67 Av", "63 Dr - Rego Park", "Woodhaven Blvd",
    "Grand Av - Newtown", "Elmhurst Av", "Jackson Hts - Roosevelt Av", "65 St",
    "Northern Blvd", "46 St", "Steinway St", "36 St", "Queens Plaza", 
    "Lexington Av/59 St", "5 Av/59 St", "57 St - 7 Av", "49 St", "Times Sq - 42 St",
    "34 St - Herald Sq", "28 St", "23 St", "14 St - Union Sq", "8 St - NYU",
    "Prince St", "Canal St", "City Hall", "Cortlandt St", "Rector St",
    "Whitehall St - South Ferry", "Court St", "Jay St - MetroTech", 
    "DeKalb Av", "Atlantic Av - Barclays Ctr", "Union St", "9 St", "Prospect Av",
    "25 St", "36 St", "45 St", "53 St", "59 St", "Bay Ridge Av", "77 St",
    "86 St", "Bay Ridge - 95 St"
]

stations_N = [
    "Astoria - Ditmars Blvd", "Astoria Blvd", "30 Av", "Broadway",
    "36 Av", "39 Av - Dutch Kills", "Queensboro Plaza", "Lexington Av/59 St",
    "5 Av/59 St", "57 St - 7 Av", "49 St", "Times Sq - 42 St",
    "34 St - Herald Sq", "28 St", "23 St", "14 St - Union Sq", "8 St - NYU",
    "Prince St", "Canal St", "City Hall", "Cortlandt St", "Rector St",
    "Whitehall St - South Ferry", "Court St", "Jay St - MetroTech", 
    "DeKalb Av", "Atlantic Av - Barclays Ctr", "36 St", "45 St", "53 St",
    "59 St", "8 Av", "Fort Hamilton Pkwy", "New Utrecht Av", "18 Av", 
    "20 Av", "Bay Pkwy", "Kings Hwy", "Avenue U", "86 St", "Coney Island - Stillwell Av"
]

stations_D = [
    "Norwood - 205 St", "Bedford Park Blvd", "Kingsbridge Rd", "Fordham Rd",
    "182-183 Sts", "Tremont Av", "174-175 Sts", "170 St", "167 St", "161 St - Yankee Stadium",
    "155 St", "145 St", "7 Av", "47-50 Sts - Rockefeller Ctr", "42 St - Bryant Pk",
    "34 St - Herald Sq", "23 St", "14 St", "W 4 St - Washington Sq", "Broadway-Lafayette St",
    "Grand St", "Atlantic Av - Barclays Ctr", "36 St", "9 Av", "Fort Hamilton Pkwy", 
    "50 St", "55 St", "62 St", "71 St", "79 St", "18 Av", "20 Av", "Bay Pkwy", 
    "25 Av", "Bay 50 St", "Coney Island - Stillwell Av"
]

# Додавання станцій і ліній до графа
for line, stops in [('R', stations_R), ('N', stations_N), ('D', stations_D)]:
    for i in range(len(stops) - 1):
        G.add_edge(stops[i], stops[i + 1], line=line)

# Функція для DFS
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
    return None

# Функція для BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            if neighbor == goal:
                return new_path
    return None

# Вхідні дані для алгоритмів
start_station = "Forest Hills - 71 Av"
goal_station = "Coney Island - Stillwell Av"

# Виконання DFS та BFS
dfs_path = dfs(G, start_station, goal_station)
bfs_path = bfs(G, start_station, goal_station)

# Результати
print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")

# Порівняння результатів
if dfs_path == bfs_path:
    print("Both DFS and BFS found the same path.")
else:
    print("DFS and BFS found different paths.")
    print("DFS Path Length:", len(dfs_path) - 1)
    print("BFS Path Length:", len(bfs_path) - 1)
