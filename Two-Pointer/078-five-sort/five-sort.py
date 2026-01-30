# def five_sort(nums):
#   i = 0
#   j = len(nums) - 1
#   while i <= j:
#     if nums[j] == 5:
#       j -= 1
#     elif nums[i] == 5:
#       nums[j], nums[i] = nums[i], nums[j]
#       i += 1
#     else:
#       i += 1
#   return nums




def five_sort(nums):
  l=0
  r=len(nums)-1
  while l < r:
    if nums[r]==5:
      r-=1
    elif nums[l]==5:
      nums[r],nums[l]=nums[l],nums[r]
      r-=1
      l+=1
    else:
      l+=1











