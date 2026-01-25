from collections import deque
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
# dfs iterative
# def tree_min_value(root):
#   min= float('inf')
#   stack= [root]
#   while stack:
#     current= stack.pop()
#     if current.val<min:
#       min= current.val
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)
#   return min
# bfs iterative
# def tree_min_value(root):
#   min= float('inf')
#   queue= deque([root])
#   while queue:
#     current= queue.popleft()
#     if current.val<min:
#       min= current.val
#     if current.right:
#       queue.append(current.right)
#     if current.left:
#       queue.append(current.left)
#   return min
# dfs recursive
# def tree_min_value(root):
#   if not root:
#     return float('inf')
#   return min(root.val, tree_min_value(root.left), tree_min_value(root.right))  
  
# a = Node(3)
# b = Node(11)
# c = Node(4)
# d = Node(4)
# e = Node(-2)
# f = Node(1)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #       3
# #    /    \
# #   11     4
# #  / \      \
# # 4   -2     1
# print(tree_min_value(a)) # -> -2  

def tree_min_values(root):
  if not root:
    return float('inf')
  return min(root.val, tree_min_values(root.left), tree_min_values(root.right))  