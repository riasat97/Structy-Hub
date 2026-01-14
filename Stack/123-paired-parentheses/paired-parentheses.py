# def paired_parentheses(string):
#   count=0
#   for ch in string:
#     if ch=="(":
#       count+=1
#     elif ch==")":
#       if count==0:
#         return False
#       count-=1
  
#   return count==0

def paired_parentheses(string):
  stack=[]
  dic={"(":")"}
  for ch in string:
    if ch in dic:
      stack.append(dic[ch])
    elif ch==")":
      if stack and stack[-1]==")":
        stack.pop()
      else:
        return False
  return len(stack)==0



      