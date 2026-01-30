# def compress(s):
#   s+='!'
#   res=[]
#   i=0
#   j=0
#   while j < len(s):
#    if s[j]==s[i]:
#      j+=1
#    else:
#      num= len(s[i:j])
#      #num= j-i
#      if num==1:
#        res.append(s[i])
#      else:
#        res.append(str(num)+s[i])
#      i=j
#   return ''.join(res)

#print(compress('ccaaatsss'))


def compress(s):
  s=s+'!'
  i=0
  j=0
  res=[]
  while i < len(s):
    if s[i]==s[j]:
      i+=1
    else:
      num_ch=len(s[j:i])
      if num_ch==1:
        res.append(s[j])
      else:
        res.append(str(num_ch)+s[j])
      j=i
  return ''.join(res)




#  What pattern is this?

# This is the same pattern family as uncompress, but the inverse operation.

# Pattern name

# Two Pointers – Run-Length Encoding (RLE) / Group Compression

# More generally:

# Two pointers for grouping consecutive characters

# How your code works (clear explanation)
# Key idea

# j → start of a group

# i → scans forward to find the end of the group

# When characters change, process the group [j : i)

# Code with comments (your logic, explained)
# def compress(s):
#   s = s + '!'          # sentinel to force last group processing instead of stoping in whiile i==len(s)
#   i = 0               # scan pointer
#   j = 0               # start of current group
#   res = []

#   while i < len(s):
#     if s[i] == s[j]:
#       i += 1          # expand the group
#     else:
#       count = i - j   # size of the group

#       if count == 1:
#         res.append(s[j])            # single char stays the same
#       else:
#         res.append(str(count) + s[j])  # compress group

#       j = i            # start new group

#   return ''.join(res)

# Value walkthrough
# Input
# s = "aaabbc"


# After sentinel:

# "aaabbc!"

# Groups processed
# Group	Output
# "aaa"	"3a"
# "bb"	"2b"
# "c"	"c"

# Final result:

# "3a2bc"

# Why the sentinel (!) is important

# Without it:

# The last group would never be processed

# Because the loop only processes when a change happens

# The sentinel forces a mismatch at the end.

# This is a common and accepted interview technique.

# Time and Space Complexity
# Time

# Single scan of string → O(n)

# Appending to result proportional to output size

# ✅ Time: O(n)

# Space

# Result array stores compressed string

# Worst case (all unique): same size as input

# ✅ Space: O(n)

# How this relates to uncompress
# Function	Operation	Pattern
# uncompress	expand counts → chars	Two-pointer parsing
# compress	chars → counts	Two-pointer grouping
# They are mirror problems.


# Similar & commonly asked problems (very close)

# These use the same idea:

# Count and Say (LeetCode 38)

# String Compression (LeetCode 443)

# Run-Length Encoding

# Basic String Parsing

# Interview memory line (very useful)

# “I scan the string with two pointers to group consecutive characters and compress each group.”













