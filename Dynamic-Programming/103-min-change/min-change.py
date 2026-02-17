def min_change(amount,coins):
  possible= _min_change(amount,coins,{})
  return possible if possible!=float('inf') else -1

def _min_change(amount, coins,memo):
  # - for each coin to reach the amount, subtract until 0 recursively
  # - base case if amount reaches to zero then return 0
  # - base case if amount less than 0 than return +inf to cancel it out of consideration while doing min amount check as that coin won't make amount 
  if amount==0:
    return 0
  if amount<0:
    return float("inf")

  min=float("inf")
  for coin in coins:
    remainder=amount-coin
    possible=1+ _min_change(remainder,coins,memo)
    if possible<min:
      min= possible
  memo[amount]=min
  return min
    
    
