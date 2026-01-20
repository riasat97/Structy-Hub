def anagrams(s1, s2):
  return count_char(s1)==count_char(s2)

def count_char(s):
  count={}
  for ch in s:
    if ch not in count:
      count[ch]=0
    count[ch]+=1
  return count