from collections import deque
# def undirected_path(edges, node_A, node_B):
#  graph=build_graph(edges)
#  return has_path(graph,node_A,node_B)

# def has_path(graph,src,dst,visited):
#   if src==dst:
#     return True
#   if src in visited:
#     return False
#   visited.add(src) 
#   for neighbour in graph[src]:
#     if has_path(graph,neighbour,dst,visited)== True:
#       return True
#   return False
# def has_path(graph,src,dst):
#   visited= {src}
#   queue= deque([src])
#   while queue:
#     current= queue.popleft()
#     if current==dst:
#       return True
#     for neighbour in graph[current]:
#       if neighbour not in visited:
#         visited.add(neighbour)
#         queue.append(neighbour)
#   return False


# def build_graph(edges):
#   graph={}
#   for edge in edges:
#     a,b= edge
#     if a not in graph:
#       graph[a]= []
#     if b not in graph:
#       graph[b]= []
#     graph[a].append(b)
#     graph[b].append(a)
#   return graph
      

# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# print(undirected_path(edges, 'j', 'm')) # -> True

def undirected_path(edges, node_A, node_B):
  graph=build_graph(edges)
  return has_path(graph,graph,des,set())

def has_path(graph,src,des,visited):
  if src==des:
    return True
  if src in visited:
    return False
  visited.add(src)
  for neighbour in graph[src]:
    if has_path(graph,neighbour,des,visited)==True:
      return True
  return False

def build_graph(edges):
  graph={}
  for edge in edges:
    a,b=edge
    if a not in graph:
      graph[a]=[]
    if b not in graph:
      graph[b]=[]
    graph[a].append(b)
    graph[b].append(a)
  return graph

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
    