#it is only for undirected graph
#In General  "spanning" means:Covering all the parts of something.
#In the case of a spanning tree:
#Spanning" means the tree reaches (covers) all the vertices of the graph.
#You're not skipping any node — every node is included and connected.
#The basic idea of a Spanning Tree is:A spanning tree is a subgraph of a connected graph that includes all the vertices and 
#forms a tree — meaning no cycles and the minimum number of edges needed to keep all nodes connected.

#There are two ways to find minimum spanning tree:
#Prim's Algorithm
#Data structure used in  prims algorithm   are  priority Priority Queue - for picking smallest edge  and we use set or list for tracking visited nodesa and adj list for input
import heapq

def prims(graph):
    vist = set()
    min_heap = []  
    result = []
    heapq.heappush(min_heap, (0, 0, -1))  # (weight, node, parent)

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node not in vist:
            vist.add(node)
        if parent != -1:
            result.append((parent, node, weight))

            
        for neighbor, edge_weight in graph[node]:
            if neighbor not in vist:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    print("Minimum Spanning Tree:")
    total_weight = 0
    for u, v, w in result:
        print(f"{u}-{v}:{w}")
        total_weight += w
    print("Total cost of MST:", total_weight)

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

prims(graph)
#krushkal
