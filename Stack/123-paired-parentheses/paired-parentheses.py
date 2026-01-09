def paired_parentheses(string):
  count=0
  for ch in string:
    if ch=="(":
      count+=1
    elif ch==")":
      if count==0:
        return False
      count-=1
  
  return count==0

