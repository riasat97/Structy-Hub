# def pair_sum(numbers, target_sum):
#   for i in range(0,len(numbers)):
#     for j in range(i+1,len(numbers)):
#       if numbers[i]+numbers[j]==target_sum:
#         return (i,j)
# o(n2)
# def pair_sum(numbers, target_sum):
#   previous = {}
#   for i in range(len(numbers)):
#     complement = target_sum - numbers[i]
#     if complement in previous:
#       return (previous[complement], i)
#     previous[numbers[i]] = i
# def pair_sum(numbers, target_sum):
#   previous={}
#   for index,num in enumerate(numbers):
#     complement= target_sum - num
#     if complement in previous:
#       return (previous[complement],index)
#     previous[num]=index

# “For each number, I calculate the complement needed to reach the target and check if it has already been seen using a hash map; if so, I return their indices.”

# n = length of numbers list
# Time: O(n)
# Space: O(n)

def pair_sum(numbers, target_sum):
  seen={}
  for index,num in enumerate(numbers):
    complement= target_sum-num
    if complement in seen:
      return (seen[complement],index)
    seen[num]=index


    
    