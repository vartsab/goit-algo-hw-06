# goit-algo-hw-06

# Graphs

## Introduction
This project explores and compares depth-first search (DFS) and breadth-first search (BFS) algorithms on a graph representing the Metropolitan Transportation Authority's D, N, and R train lines in New York City. The graph has uniform edge weights, representing the transit network within the metropolitan area. The aim is to analyze and demonstrate the differences in pathfinding strategies between DFS and BFS on this public transportation system.

## Algorithms
### Depth-First Search (DFS). 
DFS dives deep into the graph by exploring each adjacent station fully before backtracking. This strategy may uncover a path that is longer or less direct. It can also identify the most deeply nested path to the destination, even when shorter routes are available.
### Breadth-First Search (BFS). 
BFS examines all stations at the current level before moving to the next level. This method ensures the shortest path is found when all edges have equal weights, as it always locates the path with the fewest edges.

## Comparison and Conclusions
DFS and BFS identified different paths (23 and 18 respectively) due to their unique methods. DFS may find a longer route because it explores each path deeply before backtracking, while BFS always locates the shortest path, as it considers all paths at each level first.
### Conclusions
BFS is optimal for finding the shortest path by the number of edges, making it ideal for identifying the most efficient routes. Conversely, DFS might choose a longer path as it explores deeper before considering alternative routes.