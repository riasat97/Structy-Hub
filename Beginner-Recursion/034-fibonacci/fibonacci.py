def fibonacci(n):
  if n<=1:
    return n
  return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(7))
# 5  0 1 1 2 3 5 8 13 21
# 4 3 
# 3 2   2 1
# 2 1 1 0  1 0 1
# 1 0
# 1 1 1 1 1