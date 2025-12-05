def pair_product(numbers, target_product):
  previous = {}
  for key, num in enumerate(numbers):
    complement = target_product / num
    if complement in previous:
      return (key, previous[complement])
    previous[num] = key


res = pair_product([3, 2, 5, 4, 1], 8)  # -> (1, 3)
print(res)
