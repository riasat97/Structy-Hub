def all_unique(items):
  items_set = set(items)
  if len(items) > len(items_set):
    return False
  return True


# res=all_unique(["q", "r", "s", "a", "r", "z"]) # -> False
# print(res)
