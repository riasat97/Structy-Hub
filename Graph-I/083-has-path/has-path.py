from collections import deque
# dfs recursive
# def has_path(graph, src, dst):
#   if src==dst:
#     return True
#   for neighbour in graph[src]:
#     if has_path(graph,neighbour,dst)== True:
#       return True
#   return False
# breadth first
def has_path(graph, src, dst):
  queue = deque([src])
  while queue:
    current = queue.popleft()
    if current == dst:
      return True
    for neighbour in graph[current]:
      queue.append(neighbour)
  return False


# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# print(has_path(graph, 'f', 'k')) # True
