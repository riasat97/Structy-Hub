# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
# dfs
# def path_finder(root, target):
#   if not root:
#    return None
#   if root.val == target:
#    return [root.val]
#   left_path=path_finder(root.left, target)
#   if left_path:
#     return [root.val, *left_path]
#   right_path=path_finder(root.right, target)
#   if right_path:
#     return [root.val, *right_path]
#   return None

# depth first w/ append
def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]


def _path_finder(root, target):
  if not root:
    return None
  if root.val == target:
    return [root.val]
  left_path = _path_finder(root.left, target)
  if left_path:
    left_path.append(root.val)
    return left_path
  right_path = _path_finder(root.right, target)
  if right_path:
    right_path.append(root.val)
    return right_path
  return None


# Here is the step-by-step breakdown for path_finder(a, 'e').

# The key to understanding this one is to realize that the path is built backwards (from the target up to the root) as the recursive calls return.

# Think of it like a chain of people holding hands. You start at the top, looking for a friend. Once the friend is found, they raise their hand, and everyone holding their hand passes that signal back up the chain, adding themselves to the list.

# The Tree Structure
# Plaintext

#        (a)
#       /   \
#     (b)   (c)
#     / \     \
#  (d)  (e)   (f)
# Target: 'e'

# The Execution Flow
# Phase 1: Searching Downwards (a -> b -> d)
# Call path_finder(a, 'e'):

# Is a the target? No.

# Action: It pauses and checks the Left side. Calls path_finder(b, 'e').

# Call path_finder(b, 'e'):

# Is b the target? No.

# Action: It pauses and checks the Left side. Calls path_finder(d, 'e').

# Call path_finder(d, 'e'):

# Is d the target? No.

# Left Check: d.left is None -> returns None.

# Right Check: d.right is None -> returns None.

# Conclusion: "I am a dead end."

# RETURN None.

# Phase 2: Success at Node e
# Back at path_finder(b, 'e'):

# The variable left_path became None (because d failed).

# Action: Now it checks the Right side. Calls path_finder(e, 'e').

# Call path_finder(e, 'e'):

# Is e the target? YES!

# Base Case Hit: It immediately creates a list with itself.

# RETURN ['e'].

# Phase 3: Building the Path Upwards (The "Unwinding")
# This is where the list construction happens.

# Back at path_finder(b, 'e'):

# It was waiting for the right side.

# The variable right_path is now ['e'].

# The Check: if right_path: is True.

# The Construction: It takes itself ('b') and adds the result from below (['e']).

# Code: ['b', *['e']] becomes ['b', 'e'].

# RETURN ['b', 'e'].

# Back at path_finder(a, 'e'):

# It was waiting for the left side (remember step 1?).

# The variable left_path is now ['b', 'e'].

# The Check: if left_path: is True.

# The Construction: It takes itself ('a') and adds the result from below.

# Code: ['a', *['b', 'e']] becomes ['a', 'b', 'e'].

# RETURN ['a', 'b', 'e'].

# Important Note on Efficiency
# Did you notice what happened to Node C and Node F? They were never touched.

# Because Node a found the target on its left side (in Step 7), the if left_path: check passed, and it immediately returned the result. The line right_path = path_finder(root.right, target) was never executed. This is what makes this algorithm efficient—it stops searching as soon as it finds the target.

# Visualizing the List Construction
# If the python syntax [root.val, *left_path] confuses you, here is exactly what it does in plain English:

# Bottom (Node e): "I found it! Here is a list: ['e']"

# Middle (Node b): "My child 'e' found it. I will put myself at the front: ['b', 'e']"

# Top (Node a): "My child 'b' found it. I will put myself at the front: ['a', 'b', 'e']"
