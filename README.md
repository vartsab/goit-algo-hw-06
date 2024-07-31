# goit-algo-hw-06

# Graphs

## Introduction
This project implements and compares depth-first and breadth-first search over a graph with uniform edge weights.

## Algorithms
### Depth-First Search (DFS). 
The DFS algorithm searches deeper into the graph, exploring all adjacent stations before backtracking. This approach can result in finding a possible path that may be longer or less direct. It can also identify the deepest path to the goal, even if shorter paths exist.
### Breadth-First Search (BFS). 
BFS explores all levels (i.e., stations one step away from the current station) before moving deeper. This method guarantees finding the shortest path when edges have uniform weights. BFS always identifies the shortest path in terms of the number of edges.

## Comparison and Conclusions
DFS and BFS found different paths, it is due to their distinct approaches. DFS may discover a longer path due to its deep search, while BFS will always find the shortest path given uniform edge weights.

### Conclusions
BFS searches for the shortest path by the number of edges, making it optimal for finding the shortest routes. DFS, on the other hand, may opt for a longer path due to its deep exploration before branching out.