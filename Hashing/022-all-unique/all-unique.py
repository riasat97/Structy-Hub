# def all_unique(items):
#   unique_itmes = set(items)
#   return len(items) == len(unique_itmes)

def all_unique(items):
 seen=set()
 for item in items:
   if item in seen:
     return False
    seen.add(item)
 return True
# res=all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
# print(res)
