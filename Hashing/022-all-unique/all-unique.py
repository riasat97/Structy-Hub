def all_unique(items):
  unique_itmes = set(items)
  return len(items) == len(unique_itmes)


# res=all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
# print(res)
