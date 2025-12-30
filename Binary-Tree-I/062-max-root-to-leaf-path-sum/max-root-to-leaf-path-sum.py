class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def max_path_sum(root):
  if not root:
    return float("-inf")
  if not root.left and not root.right:
    return root.val
  max_left= max_path_sum(root.left)
  max_right= max_path_sum(root.right)
  return root.val+ max(max_left, max_right)