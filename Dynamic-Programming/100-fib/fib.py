# def fib(n):
#   if n<=1:
#     return n
#   return fib(n-1)+fib(n-2)

def fib(n):
  return _fib(n,{})

def _fib(n,memo):
  if n in memo:
    return memo[n]
  if n<=1:
    return n
  memo[n]=_fib(n-1,memo)+_fib(n-2,memo)
  return memo[n]

# 

# I will trace:

# 👉 fib(5)

# And I will ALWAYS show:

# ✅ Current stack
# ✅ Who is waiting
# ✅ Memo state
# ✅ What just finished
# ✅ What resumes next

# No jumping. No skipping.

# We go like a debugger.

# ✅ Code (Mental Model)
# def fib(n):
#   return _fib(n,{})

# def _fib(n,memo):
#   if n in memo:
#     return memo[n]
#   if n<=1:
#     return n
#   memo[n]=_fib(n-1,memo)+_fib(n-2,memo)
#   return memo[n]

# 🔥 Start Execution
# CALL:
# fib(5)
# → calls _fib(5,{})

# STEP 1
# Stack
# _fib(5)

# Waiting For:
# _fib(4) + _fib(3)

# Memo:
# {}


# 👉 Go LEFT first → _fib(4)

# STEP 2
# Stack
# _fib(5)   waiting for (4,3)
# _fib(4)   waiting for (3,2)

# Memo
# {}


# 👉 Go LEFT → _fib(3)

# STEP 3
# Stack
# _fib(5) waiting (4,3)
# _fib(4) waiting (3,2)
# _fib(3) waiting (2,1)


# 👉 Go LEFT → _fib(2)

# STEP 4
# Stack
# _fib(5)
# _fib(4)
# _fib(3)
# _fib(2) waiting (1,0)


# 👉 Go LEFT → _fib(1)

# STEP 5 (Base Case)
# Stack
# _fib(5)
# _fib(4)
# _fib(3)
# _fib(2)
# _fib(1)


# Since n<=1 → return 1

# POP _fib(1)
# Resume _fib(2)

# Now it has:

# ✅ fib(1)=1
# ⏳ needs fib(0)

# STEP 6 (Base Case)

# Call _fib(0)

# Return 0

# POP.

# ✅ _fib(2) can finish now
# memo[2] = 1 + 0 = 1

# Memo becomes:
# {2:1}


# POP _fib(2)

# 🔥 VERY IMPORTANT MOMENT

# Notice:

# We just created knowledge.

# Future calls will NOT go deeper.

# This is where DP saves your brain.

# Resume _fib(3)

# Previously waiting for:

# fib(2) ✅
# fib(1) ⏳


# Call _fib(1).

# Base case → returns 1.

# _fib(3) finishes:
# memo[3] = 1 + 1 = 2

# Memo:
# {2:1, 3:2}


# POP.

# Resume _fib(4)

# Was waiting for:

# fib(3) ✅
# fib(2) ⏳

# Now watch the MAGIC.

# Call _fib(2)

# But…

# CHECK MEMO FIRST:
# 2 in memo → YES


# 👉 RETURN instantly.

# NO NEW STACK FRAME.

# No recursion.

# No waiting.

# Just value 1.

# _fib(4) finishes:
# memo[4] = 2 + 1 = 3


# Memo:

# {2:1, 3:2, 4:3}


# POP.

# Resume _fib(5)

# Waiting for:

# fib(4) ✅
# fib(3) ⏳


# Call _fib(3)

# Check memo:

# ✅ FOUND → return 2 instantly.

# Again — no recursion.

# FINAL COMPUTE
# memo[5] = 3 + 2 = 5


# Memo:

# {2:1, 3:2, 4:3, 5:5}


# POP.

# Stack empty.

# DONE ✅

# ⭐ What I Want Your Brain To Notice
# Without memo:

# Stack keeps growing again and again.

# With memo:

# Stack grows ONCE.

# After that → cache hits.

# This is why DP changes:

# O(2^n)  →  O(n)


# Massive improvement.

# 🔥 The Exact Answer To Your Earlier Confusion

# You asked:

# Why didn't fib(3) get reused immediately before?

# Now you see WHY.

# Because naive recursion has:

# 👉 Zero memory.

# Memo gives recursion a brain.

# 🧠 The Ultimate Mental Model (Use This Forever)

# When reading memo recursion:

# ALWAYS think in this order:
# 1️⃣ Check memo
# 2️⃣ Base case
# 3️⃣ Go left
# 4️⃣ Go right
# 5️⃣ Store answer

# Repeat.

# DP is NOT complicated.

# It is disciplined recursion.

# 🚨 One Advanced Insight (Most Beginners Miss This)

# Notice we stored only:

# 2,3,4,5


# NOT:

# 0,1


# Why?

# Because base cases are already O(1).

# Storing them is optional.

# Senior engineers often skip it.