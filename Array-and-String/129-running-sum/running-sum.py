# def running_sum(numbers):
#   total=0
#   result=[]
#   for num in numbers:
#     total+=num
#     result.append(total)
#   return result

# n = length of list
# Time: O(n)
# Space: O(n)
















def running_sum(numbers):
  sum=0
  res=[]
  for num in numbers:
    sum+=num
    res.append(sum)
  return res
    
