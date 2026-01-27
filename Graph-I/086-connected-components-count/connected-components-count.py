from collections import deque
# def connected_components_count(graph):
#   count=0
#   visited= set()
#   for node in graph:
#     if explore(graph,node,visited)==True:
#       count+=1
#   return count
#dfs recursive  
# def explore(graph,current,visited):
#   if current in visited:
#     return False
#   visited.add(current)  
#   for neighbour in graph[current]:
#     explore(graph,neighbour,visited)
#   return True 
# bfs iterative
# def explore(graph,node,visited):
#   if node in visited:
#     return False
#   visited.add(node)
#   queue= deque([node])
#   while queue:
#     current= queue.popleft()
#     for neighbour in graph[current]:
#       if neighbour not in visited:
#         visited.add(neighbour)
#         queue.append(neighbour)
#   return True

def connected_components_count(graph):
  count=0
  visited=set()
  for node in graph:
    if explore(graph,node,visited)==True:
      count+=1
  return count

def explore(graph,current,visited):
  if current in visited:
    return False
  visited.add(current)
  for neighbour in graph[current]:
    explore(graph,neighbour,visited)
  return True