from collections import deque
def shortest_path(edges, node_A, node_B):
  graph= build_graph(edges)
  visited= set([node_A])
  queue= deque([(node_A,0)])
  
  while queue:
    node,distance= queue.popleft()
    if node==node_B:
      return distance
    
    for neighbour in graph[node]:
      if neighbour not in visited:
       visited.add(neighbour) 
       queue.append((neighbour,distance+1))
  return -1
def build_graph(edges):
  graph={}
  for edge in edges:
    a,b= edge
    if a not in graph:
      graph[a]=[]
    if b not in graph:
      graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)
  return graph