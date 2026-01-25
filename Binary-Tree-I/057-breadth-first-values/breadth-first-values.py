from collections import deque

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


# def breadth_first_values(root):
#   if not root:
#     return []
#   values = []
#   queue = deque([root])
#   while queue:
#     current = queue.popleft()
#     values.append(current.val)
#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
#   return values


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f

# breadth_first_values(a)
#    -> ['a', 'b', 'c', 'd', 'e', 'f']

# The Time Complexity is O(n) because we traverse every node once.
# The Space Complexity is O(n) because we store nodes in a queue level-by-level. 

# In a full, balanced tree, the widest level can hold a significant portion of the total nodes, so the queue size grows linearly with the width of the tree.
# Important Note: Mention that to keep this $O(n), you should use a deque so that removing the front node is O(1).

def breadth_first_values(root):
 if not root:
   return []
 queue=deque([root])
 values=[]
 while queue:
   current= queue.popleft()
   values.append(current.val)
   if current.left:
     queue.append(current.left)
   if current.right:
     queue.append(current.right)
 return values






  
