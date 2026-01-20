def most_frequent_char(s):
  char_freq={}
  for ch in s:
    # if ch not in char_freq:
    #   char_freq[ch]=0
    # char_freq[ch]+=1
    char_freq[ch]=char_freq.get(ch,0)+1
  max=None
  for ch in s:
    if max is None or char_freq[ch]>char_freq[max]:
      max=ch
  return max    

#   | Structure | Lookup | Insert | Delete | Ordered? | Duplicates |
# | --------- | ------ | ------ | ------ | -------- | ---------- |
# | List      | O(n)   | O(n)   | O(n)   | ✅        | ✅          |
# | Set       | O(1)   | O(1)   | O(1)   | ❌        | ❌          |
# | Dict      | O(1)   | O(1)   | O(1)   | ✅ (keys) | ❌ (keys)   |


