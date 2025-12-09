def all_unique(items):
  prev={}
  for key,item in enumerate(items):
    if item in prev:
      return False
    prev[item]= key
  return True
#res=all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
#print(res)