def reverse_some_chars(s, chars):
  chars_set=set(chars)
  stack=[]
  res=[]
  for ch in s:
    if ch in chars_set:
      stack.append(ch)
  for ch in s:
    if ch in chars_set:
      res.append(stack.pop())
    else:
      res.append(ch)
  return ''.join(res)
      