from collections import deque
# def largest_component(graph):
#   largest=0
#   visited=set()
#   for node in graph:
#     res=explore(graph,node,visited)
#     if res>largest:
#       largest=res
#   return largest

# def explore(graph,current,visited):
#   if current in visited:
#     return 0
#   visited.add(current)
#   size=1
#   for neighbour in graph[current]:
#     size+=explore(graph,neighbour,visited)
#   return size
# bfs iterative
# def explore(graph, src, visited):
#   if src in visited:
#     return 0
#   visited.add(src)  
#   queue= deque([src])
#   size=0
#   while queue:
#     current= queue.popleft()
#     size+=1 # cause need to count src node
#     for neighbour in graph[current]:
#       if neighbour not in visited:
#         visited.add(neighbour)
#         queue.append(neighbour)
#   return size
















def largest_component(graph):
  largest=0
  visited=set()
  for node in graph:
    size=explore(graph,node,visited)
    if size>largest:
      largest=size
  return largest

def explore(graph,node,visited):
  if node in visited:
    return 0
  visited.add(node)
  size=1
  for neighbour in graph[node]:
    size+=explore(graph,neighbour,visited)
  return size
    





  