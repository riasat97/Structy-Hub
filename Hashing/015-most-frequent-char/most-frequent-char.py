def most_frequent_char(s):
  count_char={}
  for char in s:
    if char not in count_char:
     count_char[char]=0
    count_char[char]+=1
  max=s[0]
  for char in count_char:
    if count_char[char]> count_char[max]:
      max= char
  return max
  pass # todo


#   | Structure | Lookup | Insert | Delete | Ordered? | Duplicates |
# | --------- | ------ | ------ | ------ | -------- | ---------- |
# | List      | O(n)   | O(n)   | O(n)   | ✅        | ✅          |
# | Set       | O(1)   | O(1)   | O(1)   | ❌        | ❌          |
# | Dict      | O(1)   | O(1)   | O(1)   | ✅ (keys) | ❌ (keys)   |


