# from collections import Counter
# def subarray_sum_count(numbers, target_sum):
#   total=0
#   prefix_sums=[0]
#   for num in numbers:
#     total+=num
#     prefix_sums.append(total)

#   count=0
#   seen= Counter()
#   for b in prefix_sums:
#     a=b-target_sum
#     count+=seen[a]
#     seen[b]+=1
#   return count

# n = length of numbers
# Time: O(n)
# Space: O(n)



# b-a=target
# a= b-target
# list [1, 3, 1, 4, 3]
# pre   0, 1, 4, 5, 9, 12  target=5
#       a         b 
#             a     b
from collections import Counter
def subarray_sum_count(numbers, target_sum):
  total=0
  prefix_sums=[0]
  for num in numbers:
    total+=num
    prefix_sums.append(total)
  seen=Counter()
  count=0
  for b in prefix_sums:
    a=b-target_sum
    if a in seen:
      count+=seen[a]
    seen[b]+=1
  return count 


  