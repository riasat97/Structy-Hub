def largest_component(graph):
  largest=0
  visited=set()
  for node in graph:
    res=explore(graph,node,visited)
    if res>largest:
      largest=res
  return largest

def explore(graph,current,visited):
  if current in visited:
    return 0
  visited.add(current)
  size=1
  for neighbour in graph[current]:
    size+=explore(graph,neighbour,visited)
  return size