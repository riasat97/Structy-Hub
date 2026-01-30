# def is_palindrome(s):
#   i = 0
#   j = len(s) - 1
#   while i < j:
#     if s[i] != s[j]:
#       return False
#     i += 1
#     j -= 1
#   return True

def is_palindrome(s): 
  l=0
  r=len(s)-1
  while l<r:
    if s[l]!=s[r]:
      return False
  return True





























