# Graph data structures is implemented with two approaches:
#1. Adjacency Matrix
#2.Adjacency List:it is mostly used 
# Graph   Operation 
# 1.Graph Traversal:
# 2.Pathfinding: 
# 3.Cycle Detection:
# 4.Topological Sorting:
# 5.Graph Representation Conversions: 
# 6.Graph Connectivity:
# 7.Graph Coloring:
# 8.Spanning Tree: 
# 9.Graph Isomorphism:
# 10.Edge Operations:

# GRAPH REPRESENTATION
#Adj Matrix
matrix = [
    [0, 1, 1],  # Edges from vertex 0 to 1 and 2
    [1, 0, 0],  # Edge from vertex 1 to 0
    [1, 0, 0]   # Edge from vertex 2 to 0
]
# adj list
#dict
adj_list = {
    0: [1, 2],
    1: [0],
    2: [0]
}
#list in a list
adj_list = [
    [1, 2],  # Neighbors of vertex 0
    [0],     # Neighbors of vertex 1
    [0]      # Neighbors of vertex 2
]
