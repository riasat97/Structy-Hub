def befitting_brackets(string):
  dic={"(":")", "{":"}", "[":"]"}
  stack=[]
  for ch in string:
    if ch in dic:
      stack.append(dic[ch])
    else:
      if stack and ch==stack[-1]:
        stack.pop()
      else:
        return False
  return len(stack)==0
