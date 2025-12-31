def undirected_path(edges, node_A, node_B):
 graph=build_graph(edges)
 return has_path(graph,node_A,node_B,set())

def has_path(graph,src,dst,visited):
  if src==dst:
    return True
  if src in visited:
    return False
  visited.add(src) 
  for neighbour in graph[src]:
    if has_path(graph,neighbour,dst,visited)== True:
      return True
  return False

def build_graph(edges):
  graph={}
  for edge in edges:
    a,b= edge
    if a not in graph:
      graph[a]= []
    if b not in graph:
      graph[b]= []
    graph[a].append(b)
    graph[b].append(a)
  return graph
      

# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]

# print(undirected_path(edges, 'j', 'm')) # -> True