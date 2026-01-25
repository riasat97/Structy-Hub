# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


# def depth_first_values(root):
#   if not root:
#     return []
#   stack= [root]
#   values= []
#   while stack:
#     current= stack.pop()
#     values.append(current.val)
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)
#   return values


# def depth_first_values(root):
#   if not root:
#     return []

#   left_values = depth_first_values(root.left)
#   right_values = depth_first_values(root.right)
#   return [root.val, *left_values, *right_values]


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# print(depth_first_values(a))

# The Time Complexity is $O(n) because we must visit every node exactly once.
# The Space Complexity is $O(h), where h is the height of the tree. 
# This is because the stack (either the Call Stack in recursion or my manual stack) only grows as deep as the current path we are exploring. we only need to store the current branch.
#------------------------------------------
# The space complexity is determined by how many nodes the computer has to "remember" at the same time while diving deep into a branch.
# Space$O(h) We only store the current path on the stack; memory use is proportional to the tree's height".

# In the worst case—a skewed tree—this is $O(n). 
# In the best case—a balanced tree—this is $O(log n).
#------------------------------------------
# Why the "Worst Case" matters:
# In an interview, always add that in the worst-case scenario (a skewed tree that looks like a line), the height $h$ is equal to $n$, making the space complexity $O(n)$. In the best-case scenario (a balanced, bushy tree), the height is much smaller, making the space complexity $O(\log n)$.

class Node:
  def __init__(self,val):
    self.val= val
    self.left= None
    self.right= None
    
# def depth_first_values(root):
#   stack=[root]
#   values=[]
#   while stack:
#     current= stack.pop()
#     values.append(current.val)
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)
#   return values
  
def depth_first_values(root):
  if not root:
    return []
  left_values= depth_first_values(root.left)
  right_values= depth_first_values(root.right)
  return [root.val,*left_values, *right_values]




  


    