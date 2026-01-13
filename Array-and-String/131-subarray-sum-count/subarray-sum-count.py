from collections import Counter
def subarray_sum_count(numbers, target_sum):
  total=0
  prefix_sums=[0]
  for num in numbers:
    total+=num
    prefix_sums.append(total)

  count=0
  seen= Counter()
  for b in prefix_sums:
    a=b-target_sum
    count+=seen[a]
    seen[b]+=1