def running_sum(numbers):
  total=0
  result=[]
  for num in numbers:
    total+=num
    result.append(total)
  return result