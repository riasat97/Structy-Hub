def decompress_braces(string):
  stack=[]
  nums="123456789"
  for ch in string:
    if ch in nums:
      stack.append(int(ch))
    else:
      if ch=="}":
        segment=''
        while isinstance(stack[-1],str):
          popped= stack.pop()
          segment= popped+segment
        num= stack.pop()
        stack.append(segment*num)
      elif ch!="{":
        stack.append(ch)
  return ''.join(stack)
