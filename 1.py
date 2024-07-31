import networkx as nx
import matplotlib.pyplot as plt

# Об'явлення графа
G = nx.Graph()

# Додавання станцій (вершин) та ліній (ребер)
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

# Додавання станцій і ліній до графа
for line, stops in [('R', stations_R), ('N', stations_N), ('D', stations_D)]:
    for i in range(len(stops) - 1):
        G.add_edge(stops[i], stops[i + 1], line=line)

# Аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())
average_degree = sum(degree_dict.values()) / num_nodes

print(f"Number of stations (nodes): {num_nodes}")
print(f"Number of connections (edges): {num_edges}")
print(f"Average degree of stations: {average_degree:.2f}")

# Виведення ступеня кожної вершини
for station, degree in degree_dict.items():
    print(f"Station {station}: Degree {degree}")

# Візуалізація графа
plt.figure(figsize=(15, 15))
pos = nx.spring_layout(G, seed=42)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['line'] for u, v, d in G.edges(data=True)})
plt.title("New York City Subway Map - R, N, D Lines")
plt.show()