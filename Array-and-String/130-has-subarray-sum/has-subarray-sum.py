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