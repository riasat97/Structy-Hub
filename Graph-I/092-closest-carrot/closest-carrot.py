from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  # BFS queue holds: (row, col, distance_from_start)
  queue = deque([(starting_row, starting_col, 0)])
  visited = set([(starting_row, starting_col)])

  while queue:
    row, col, dist = queue.popleft()

    # If we reached a carrot, BFS guarantees it's the shortest distance
    if grid[row][col] == "C":
      return dist

    # Explore 4 directions
    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in deltas:
      nr, nc = row + dr, col + dc

      # Check valid cell: inside bounds, not wall, not visited
      if is_inbounds(grid, nr, nc) and grid[nr][nc] != "X" and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append((nr, nc, dist + 1))

  # No carrot reachable
  return -1


def is_inbounds(grid, row, col):
  return 0 <= row < len(grid) and 0 <= col < len(grid[0])

# Time and Space Complexity (interview-friendly)

# Let R = rows, C = cols, total cells = R*C.

# Time: O(R*C)
# because each cell can enter the queue at most once, and each visit checks 4 neighbors.

# Space: O(R*C)
# for the visited set + queue in worst case.


# Closest Carrot (Shortest path in a grid)
# Simple idea

# You want the shortest path from the start cell to any carrot C, moving only up/down/left/right, avoiding walls X.

# ✅ Best tool: BFS (Breadth-First Search)
# Because BFS explores level-by-level (distance 0, then 1, then 2…), the first time you reach a C is guaranteed to be the shortest path.

# Approach (how to do it)

# Put the starting cell in a queue with distance 0

# Use a visited set so you don’t revisit cells

# While queue is not empty:

# pop the front

# if it’s a carrot → return distance

# push all valid neighbors (inside grid, not wall, not visited) with distance + 1

# If BFS finishes without finding carrot → return -1  

# One-liner “trick” to remember in interviews

# “Shortest path in an unweighted grid = BFS with queue + visited.”

# (And “unweighted” here means every move costs 1.)

# Top related problems (same concept)

# These all use BFS in a grid / shortest path / visited:

# Shortest Path in Binary Matrix (LeetCode 1091)

# Rotting Oranges (LeetCode 994) — multi-source BFS

# Number of Islands (LeetCode 200) — BFS/DFS + visited

# Flood Fill (LeetCode 733)

# Walls and Gates (LeetCode 286)

# 01 Matrix (LeetCode 542) — multi-source BFS

# Maze / Nearest Exit from Entrance in Maze (LeetCode 1926)

# the step-by-step queue state for sample grid to “see” why the answer becomes 4.

# We start from:

# Start = (1,2)
# Goal = nearest 'C'


# Grid (visualized):

# O O O O O
# O X S O O
# O X X O O
# O X C O O
# C O O O O


# S = start (1,2)

# 🔥 BFS Visualization (Queue Movement)

# Think of BFS like water spreading outward level by level.

# ✅ Distance = 0

# Queue:

# [(1,2,0)]


# Visited:

# (1,2)


# Cells reachable in 1 move:

# Up → (0,2)

# Right → (1,3)

# Left → blocked by X

# Down → blocked by X

# ✅ Distance = 1

# Queue:

# [(0,2,1), (1,3,1)]


# Visited grows.

# Now expand each:

# From (0,2):

# (0,1)

# (0,3)

# From (1,3):

# (2,3)

# (1,4)

# Queue becomes:

# [(0,1,2), (0,3,2), (2,3,2), (1,4,2)]

# ✅ Distance = 2

# Expand again:

# From (2,3) we unlock something important:

# 👉 neighbor → (3,3)

# Queue:

# [(0,1,2), (0,3,2), (2,3,2), (1,4,2),
#  (0,0,3), (0,4,3), (3,3,3), (2,4,3)]

# ✅ Distance = 3

# Now expand (3,3):

# Neighbors:

# 👉 LEFT → (3,2)
# Which is…

# 🎯 CARROT!

# So we return:

# distance = 4


# (Because carrot is added as dist + 1)

# ⭐ Why BFS ALWAYS finds shortest path

# Imagine drawing circles outward:

# distance 0 → start
# distance 1 → all neighbors
# distance 2 → neighbors of neighbors


# You cannot accidentally reach a longer path first.

# DFS ❌ might go deep into a long maze.
# BFS ✅ guarantees shortest.

# 🧠 Interview Brain Trick (VERY important)

# When you see:

# ✅ grid
# ✅ shortest path
# ✅ no weights
# ✅ move in 4 directions

# 👉 Your brain should scream:

# 👉 BFS!!!
# 🔥 Pattern Recognition (Senior-level tip)

# Immediately convert grid → graph mentally:

# Each cell = node
# Edges = up/down/left/right

# Now the question becomes:

# 👉 “Shortest path in an unweighted graph?”

# Answer = BFS.

# ⚠️ Most Common Mistake

# People mark visited after popping.

# ❌ Wrong — causes duplicates in queue.

# Always:

# ✅ mark visited when pushing into queue

# You did this correctly 👍 (seriously — many candidates fail here).

# ⭐ Ultra-short Memory Version

# If interviewer rushes you:

# “Use BFS from start, push neighbors with distance, stop when carrot found.
# Time O(rows * cols), space O(rows * cols).”

# Done. Strong answer.

# If you want next-level mastery, I strongly recommend learning these 3 together:

# 👉 Number of Islands → Flood Fill → Rotting Oranges

# Once your brain connects them, 90% of grid problems become easy.