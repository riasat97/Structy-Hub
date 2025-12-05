def exclusive_items(a, b):
  diff=[]
  set_a= set(a)
  set_b= set(b)
  for item in a:
    if item not in set_b:
      diff.append(item)
  for ele in b:
    if ele not in set_a:
      diff.append(ele)
  return diff
#print(exclusive_items([4,2,1,6], [3,6,9,2,10])) # -> [4,1,3,9,10])
 