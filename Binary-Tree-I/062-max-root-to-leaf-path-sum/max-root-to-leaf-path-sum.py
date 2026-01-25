class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# def max_path_sum(root):
#   if not root:
#     return float("-inf")
#   if not root.left and not root.right:
#     return root.val
#   max_left= max_path_sum(root.left)
#   max_right= max_path_sum(root.right)
#   return root.val+ max(max_left, max_right)


#for each subtree add myself(root) to the bigger of my children value.



#   Plaintext

#        (a) 3
#       /     \
#   (b) 11    (c) 4
#     /  \       \
#  (d) 4 (e)-2   (f) 1
# The Execution Flow (The "Call Stack")
# Imagine a stack of index cards. Every time we call a function, we add a card to the top. When we return, we remove the card and give the answer to the card below it.

# Phase 1: Go Deep Left (a -> b -> d)
# Call max_path_sum(a): We start at the root 3.

# It is not a leaf. It pauses and calls its left child.

# Call max_path_sum(b): We are at 11.

# It is not a leaf. It pauses and calls its left child.

# Call max_path_sum(d): We are at 4.

# Leaf Check: root.left and root.right are both None.

# Action: It hits the base case!

# RETURN 4. (Node d is popped off the stack).

# Phase 2: Finish Node b's Children (d done, now e)
# Back at max_path_sum(b):

# It received 4 from the left.

# Now it calls its right child.

# Call max_path_sum(e): We are at -2.

# Leaf Check: It is a leaf.

# RETURN -2. (Node e is popped off the stack).

# Phase 3: Solve Node b (11)
# Back at max_path_sum(b):

# It has max_left = 4 and max_right = -2.

# Calculation: 11 + max(4, -2).

# 11 + 4 = 15.

# RETURN 15. (Node b is popped off the stack).

# Phase 4: Back to Root, then Go Right (a -> c)
# Back at max_path_sum(a):

# It received 15 from the left side.

# Now it must process the right side to compare. It calls root.right.

# Call max_path_sum(c): We are at 4.

# It is not a leaf.

# Call Left: It calls c.left (which is None).

# Call max_path_sum(None):

# Base Case: if not root.

# RETURN -inf. (This ensures we don't pick a non-existent path).

# Back at max_path_sum(c):

# It received -inf from the left.

# Call Right: It calls c.right (Node f).

# Phase 5: Finish Node c (4) and Root (3)
# Call max_path_sum(f): We are at 1.

# Leaf Check: It is a leaf.

# RETURN 1.

# Back at max_path_sum(c):

# It has max_left = -inf and max_right = 1.

# Calculation: 4 + max(-inf, 1).

# 4 + 1 = 5.

# RETURN 5.

# Back at max_path_sum(a) (THE ROOT):

# It has finally received answers from both sides!

# Left side (from node b) returned 15.

# Right side (from node c) returned 5.

# Final Calculation: 3 + max(15, 5).

# 3 + 15 = 18.

# RETURN 18.

# Summary of Values Returned
# Node d (4): Returns 4

# Node e (-2): Returns -2

# Node b (11): Choose 4 vs -2? Chooses 4. Adds self (11). Returns 15.

# Node f (1): Returns 1

# Node c (4): Choose -inf vs 1? Chooses 1. Adds self (4). Returns 5.

# Node a (3): Choose 15 vs 5? Chooses 15. Adds self (3). Returns 18.

def max_path_sum(root):
  if not root:
    return float('-inf')
  if not root.left and not root.right:
    return root.val
  return root.val+ max(max_path_sum(root.left),max_path_sum(root.right))
  
  