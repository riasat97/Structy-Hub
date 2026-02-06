def prereqs_possible(num_courses, prereqs):
  #build graph with it's adjacency list for each no.of courses using prerequisites
  # for each node (courses) detect cycle using dfs
  # if cycle exists than completing courses not possible else possible
  visiting=set()
  visited=set()
  graph=build_graph(num_courses,prereqs)
  for node in graph:
    if detect_cycle(graph,node,visiting,visited):
      return False
  return True

def detect_cycle(graph,node,visiting,visited):
  if node in visited:
    return False
  if node in visiting:
    return True
  visiting.add(node)
  for neighbour in graph[node]:
    if detect_cycle(graph,neighbour,visiting,visited):
      return True
  visiting.remove(node)
  visited.add(node)
  return False

def build_graph(n,prereqs):
  graph={}
  for i in range(n):
    graph[i]=[]
  for a,b in prereqs:
    graph[a].append(b)
  return graph
    