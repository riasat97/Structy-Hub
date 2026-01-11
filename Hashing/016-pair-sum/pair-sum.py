def pair_sum(numbers, target_sum):
  for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
      if numbers[i]+numbers[j]==target_sum:
        return (i,j)