# def five_sort(nums):
#   l=0
#   r=len(nums)-1
#   while l < r:
#     if nums[r]==5:
#       r-=1
#     elif nums[l]==5:
#       nums[r],nums[l]=nums[l],nums[r]
#       r-=1
#       l+=1
#     else:
#       l+=1
#   return nums

# n = array size
# Time: O(n)
# Space: O(1)

def five_sort(nums):
  k=0
  for i in range(len(nums)):
    if nums[i]!=5:
      nums[k]=nums[i]
      k+=1
  for i in range(k,len(nums)):
    nums[i]=5
    









