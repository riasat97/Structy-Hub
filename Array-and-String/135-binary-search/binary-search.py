def binary_search(numbers, target):
  lo=0
  hi= len(numbers)-1
  while (lo<=hi):
    mid= (lo+hi)//2
    val= numbers[mid]
    if val == target:
      return mid
    elif target < val:
      hi= mid-1
    else:
      lo=mid+1
  return -1
    
    