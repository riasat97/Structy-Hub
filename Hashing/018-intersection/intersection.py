# def intersection(a, b):
#   set_a= set(a)
#   return [ item for item in b if item in set_a]
#   pass # todo

# def intersection(a, b):
#   a_set=set(a)
#   res=[]
#   for ele in b:
#     if ele in a_set:
#       res.append(ele)
#   return res
def intersection(a, b):
  a_set=set(a)
  return [ ele for ele in b if ele in set_a]