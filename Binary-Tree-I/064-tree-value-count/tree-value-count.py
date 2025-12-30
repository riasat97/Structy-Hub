# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
# dfs iterative 
def tree_value_count(root, target):
  if not root:
    return 0
  value_count=0  
  stack= [root]
  while stack:
    current= stack.pop()
    if current.val == target:
      value_count+=1
    if current.left:
      stack.append(current.left)
    if current.right:
      stack.append(current.right)
  return value_count
