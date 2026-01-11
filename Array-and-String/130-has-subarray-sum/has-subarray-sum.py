#Brute Force Nested Loops O(n3)
# def has_subarray_sum(numbers, target_sum):
#   for start in range(len(numbers)):
#     for end in range(start+1,len(numbers)+1):
#       if sum(numbers[start:end])==target_sum:
#         return True
#   return False
#Brute Force Nested Loops O(n2)
def has_subarray_sum(numbers, target_sum):
  for start in range(len(numbers)):
    current_sum=0
    for end in range(start,len(numbers)):
      current_sum+=numbers[end]
      if current_sum== target_sum:
       return True
  return False
#prefix sums O(n2)
def has_subarray_sum(numbers, target_sum):
  prefix_sums=[0]
  total=0
  for num in numbers:
    total+=num
    prefix_sums.append(total)

  for start in range(len(prefix_sums)):
    for end in range(start+1,len(prefix_sums)):
      if prefix_sums[end]-prefix_sums[start] == target_sum:
        return True
  return False



  