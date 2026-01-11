#Brute Force Nested Loops
def has_subarray_sum(numbers, target_sum):
  for start in range(len(numbers)):
    for end in range(start+1,len(numbers)+1):
      if sum(numbers[start:end])==target_sum:
        return True
  return False