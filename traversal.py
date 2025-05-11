# In graph there two traversal 
#BFS #DFS

#Basic idea of BFS:BFS (Breadth-First Search) explores a graph level by level. It starts at a node, visits all its neighbors first, then their neighbors, and so on — like spreading out in waves.
#data structures used in bfs is queue -FIFO - for traversal and we can use list or set for tracking visited nodes
from collections import deque

def bfs(graph, start):
    visit = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.add(node)
        if node in graph:  
            for neighbor in graph[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
    return visit

graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]  
}
result = bfs(graph, 0)
print(result)
#DFS
#Basic idea of DFS:DFS (Depth-First Search) explores a graph by going deep into one path first, and only comes back when it can’t go further — then it tries other paths.
#data structutres used for dfs is DFS Stack-LiFO -for traversal and we can use list or set for tracking visited nodes.
# this can be impleted in two ways 
#iterative
def dfs(graph,start):
  visit=set()
  stack = [start]
  while stack:
     node =stack.pop()
     if node not in visit:
        print(node)
        visit.add(node)
       
     for n in reversed(graph[node]):
         if n not in visit:
          stack.append(n)
  
       
graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
dfs(graph, 'A')
# recursion
graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')
