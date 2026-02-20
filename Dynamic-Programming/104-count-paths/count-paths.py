def count_paths(grid):
    # Start recursion from top-left corner
    return _count_paths(grid, 0, 0, {})
  
def _count_paths(grid, r, c, memo):
    pos = (r, c)
    # If already computed, return stored value
    if pos in memo:
        return memo[pos]
    # Base Case 1: Out of bounds OR hit wall
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return 0
    # Base Case 2: Reached bottom-right
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    # Recursive calls
    down = _count_paths(grid, r + 1, c, memo)
    right = _count_paths(grid, r, c + 1, memo)
    # Store result in memo
    memo[pos] = down + right
    return memo[pos]

# 🧠 Time & Space Complexity
# ⏱ Time Complexity:

# O(m × n)

# Why?
# Each cell is computed once because of memoization.

# 📦 Space Complexity:

# O(m × n)

# Memo dictionary stores at most m × n entries

# Recursion stack worst case: m + n

# 🧪 Example Grid
# O O O
# O X O
# O O O


# Index reference:

# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)


# Destination = (2,2)

# 🔍 Now Follow EXACT Code Execution Order

# We call:

# _count_paths(grid, 0, 0, {})

# 🔹 CALL 1 → (0,0)

# Not in memo

# Not wall

# Not destination

# So it executes:

# down = _count_paths(1,0)
# right = _count_paths(0,1)


# ⚠️ IMPORTANT:
# Python evaluates down FIRST.
# So we completely finish the DOWN branch before touching RIGHT.

# ⬇️ DOWN Branch from (0,0)
# 🔹 CALL 2 → (1,0)

# Again:

# down = _count_paths(2,0)
# right = _count_paths(1,1)

# 🔹 CALL 3 → (2,0)
# down = _count_paths(3,0)
# right = _count_paths(2,1)

# 🔹 CALL 4 → (3,0)

# Out of bounds
# Returns 0

# Back to (2,0)

# Now:

# down = 0

# 🔹 CALL 5 → (2,1)
# down = _count_paths(3,1)
# right = _count_paths(2,2)

# 🔹 CALL 6 → (3,1)

# Out of bounds → returns 0

# Back to (2,1)

# down = 0

# 🔹 CALL 7 → (2,2)

# Destination reached ✅
# Returns 1

# Back to (2,1)

# Now:

# down = 0
# right = 1

# Summation happening here:
# memo[(2,1)] = 0 + 1 = 1
# return 1


# So:

# (2,1) → 1


# Back to (2,0)

# We now have:

# down = 0
# right = 1

# Summation:
# memo[(2,0)] = 0 + 1 = 1
# return 1


# So:

# (2,0) → 1


# Back to (1,0)

# We now compute right branch:

# 🔹 CALL 8 → (1,1)

# Wall ❌
# Returns 0

# Back to (1,0)

# Now:

# down = 1
# right = 0

# Summation:
# memo[(1,0)] = 1 + 0 = 1
# return 1


# So:

# (1,0) → 1

# ⬅️ Now Back to (0,0)

# We finished DOWN branch.

# So now:

# down = 1


# Now compute RIGHT branch.

# ➡️ RIGHT Branch from (0,0)
# 🔹 CALL 9 → (0,1)
# down = _count_paths(1,1)
# right = _count_paths(0,2)

# 🔹 CALL 10 → (1,1)

# Wall ❌
# Returns 0

# Back to (0,1)

# down = 0

# 🔹 CALL 11 → (0,2)
# down = _count_paths(1,2)
# right = _count_paths(0,3)

# 🔹 CALL 12 → (1,2)
# down = _count_paths(2,2)
# right = _count_paths(1,3)

# 🔹 CALL 13 → (2,2)

# Destination → returns 1

# Back to (1,2)

# down = 1

# 🔹 CALL 14 → (1,3)

# Out of bounds → returns 0

# Back to (1,2)

# Now:

# down = 1
# right = 0

# Summation:
# memo[(1,2)] = 1 + 0 = 1
# return 1


# So:

# (1,2) → 1


# Back to (0,2)

# Now compute:

# 🔹 CALL 15 → (0,3)

# Out of bounds → returns 0

# Back to (0,2)

# Now:

# down = 1
# right = 0

# Summation:
# memo[(0,2)] = 1 + 0 = 1
# return 1


# So:

# (0,2) → 1


# Back to (0,1)

# Now:

# down = 0
# right = 1

# Summation:
# memo[(0,1)] = 0 + 1 = 1
# return 1


# So:

# (0,1) → 1

# 🔥 FINAL STEP Back to (0,0)

# Now we finally have:

# down = 1
# right = 1

# FINAL SUMMATION:
# memo[(0,0)] = 1 + 1 = 2
# return 2

# ✅ Final Answer = 2


# 🎯 The Big Idea

# Recursion goes all the way down first.

# Base cases return 0 or 1.

# Then addition happens while coming back up.

# Memo stores each computed cell.

# Final answer bubbles up to (0,0).

# 🌳 Full Tree
# (0,0)
# │
# ├── DOWN → (1,0)
# │   │
# │   ├── DOWN → (2,0)
# │   │   │
# │   │   ├── DOWN → (3,0) → 0   ❌ out of bounds
# │   │   │
# │   │   └── RIGHT → (2,1)
# │   │       │
# │   │       ├── DOWN → (3,1) → 0   ❌
# │   │       │
# │   │       └── RIGHT → (2,2) → 1  ✅ destination
# │   │
# │   │   (2,1) = 0 + 1 = 1
# │   │   (2,0) = 0 + 1 = 1
# │   │
# │   └── RIGHT → (1,1) → 0 ❌ wall
# │
# │   (1,0) = 1 + 0 = 1
# │
# └── RIGHT → (0,1)
#     │
#     ├── DOWN → (1,1) → 0 ❌ wall
#     │
#     └── RIGHT → (0,2)
#         │
#         ├── DOWN → (1,2)
#         │   │
#         │   ├── DOWN → (2,2) → 1 ✅
#         │   │
#         │   └── RIGHT → (1,3) → 0 ❌
#         │
#         │   (1,2) = 1 + 0 = 1
#         │
#         └── RIGHT → (0,3) → 0 ❌
    
#     (0,2) = 1 + 0 = 1
#     (0,1) = 0 + 1 = 1

# (0,0) = 1 + 1 = 2
