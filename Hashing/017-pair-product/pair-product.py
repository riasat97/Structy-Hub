def pair_product(numbers, target_product):
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      if numbers[i]*numbers[j]== target_product:
        return (i,j)

res=pair_product([3, 2, 5, 4, 1], 8) # -> (1, 3)
print(res)
