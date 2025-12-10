from collections import Counter
def intersection_with_dupes(a, b):
  counter_a= Counter(a)
  counter_b= Counter(b)
  res= []
  for ele in counter_a:
    for i in range(0, min(counter_a[ele],counter_b[ele])):
      res.append(ele)
  return res
  pass # todo

intersection_with_dupes(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
) # -> ["b", "b"]