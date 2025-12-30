# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  if not root:
   return None
  if root.val == target:
   return root.val
  left=path_finder(root.left, target)
  if left:
    return [root.val, *left]
  right=path_finder(root.right, target)
  if right:
    return [root.val, *right]
  return None
    
