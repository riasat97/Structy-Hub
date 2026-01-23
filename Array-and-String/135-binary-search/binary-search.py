# def binary_search(numbers, target):
  # lo=0
  # hi= len(numbers)-1
  # while (lo<=hi):
  #   mid= (lo+hi)//2
  #   val= numbers[mid]
  #   if val == target:
  #     return mid
  #   elif target < val:
  #     hi= mid-1
  #   else:
  #     lo=mid+1
  # return -1

# n = length of numbers array
# Time: O(logn)
# Space: O(1)
    
# Search in Rotated Sorted Array: https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=blind75    

# Find Minimum in Rotated Sorted Array: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=blind75

def binary_search(numbers, target):
  lo=0
  hi= len(numbers)-1
  while lo<=hi:
    mid=(lo+hi)//2
    if target==numbers[mid]:
      return mid
    elif target<numbers[mid]:
      hi=mid-1
    else:
      lo=mid+1
  return -1