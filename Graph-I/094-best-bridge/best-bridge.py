from collections import deque
def best_bridge(grid):
  #first search main land using dfs and get land cells through set
  #push all land cells to queue
  #now from main land find other land's shortest path to make bridge using bfs
   # -------------------------
  # PHASE 1: Find one island
  # -------------------------
  main_land=None
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col]=="L":
        island= explore(grid,row,col,set())
        if len(island)>0:
          main_land=island
          break
    if main_land:
        break
  #print(main_land) 
  # ------------------------------
  # PHASE 2: BFS from that island
  # Multi-source BFS: start from ALL cells in island
  # ------------------------------
  visited=set(main_land)
  queue= deque([])
  for pos in main_land:
    r,c=pos
    queue.append((r,c,0)) # (row, col, distance)
  while queue:
    r,c,dist= queue.popleft()
    # If we hit land that isn't in the first island -> we reached second island
    if grid[r][c]=="L" and (r,c) not in main_land:
      return dist-1 # subtract 1 because we don’t count stepping onto the island
    # Explore 4 directions
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
      nr=dr+r
      nc=dc+c
      npos=(nr,nc)
      if is_inbound(grid,nr,nc) and npos not in visited:
        visited.add(npos)
        queue.append((nr,nc,dist+1))
  
def explore(grid,r,c,visited): # target is find land paths
  # DFS to collect all land connected to (row, col)
  if not is_inbound(grid,r,c) or grid[r][c]=="W":
    return visited
  pos=(r,c)
  if pos in visited:
    return visited
  visited.add(pos)
  explore(grid,r+1,c,visited)
  explore(grid,r-1,c,visited)
  explore(grid,r,c-1,visited)
  explore(grid,r,c+1,visited)
  return visited
  
def is_inbound(grid,r,c):
  return 0<=r<len(grid) and 0<=c<len(grid[0])

grid = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
best_bridge(grid) # -> 1

# Time and Space Complexity (interview-ready)

# Let total cells be R*C.

# DFS island capture: visits some cells → O(R*C) worst-case

# BFS expansion: each cell enqueued at most once → O(R*C)

# ✅ Time: O(R*C)
# ✅ Space: O(R*C) (visited + queue)

# Solution:
# Simple explanation

# There are exactly 2 islands (L regions). You want the minimum number of water cells (W) you must turn into land to connect them.

# ✅ This is a shortest path / minimum expansion problem → use BFS.

# But first you must know where one island is.

# Approach (two-phase strategy)
# Phase 1: Find one full island (DFS)

# Scan the grid

# When you find land L, run DFS to collect all cells of that island

# That set is main_island

# Phase 2: Multi-source BFS expansion from that island

# Put all cells of main_island into the queue with distance 0

# Expand outward into water level-by-level

# The first time you reach a land cell L that’s not in main_island, you hit the second island

# Answer = distance - 1 (because distance counts steps including starting from land)

# This works because BFS guarantees the first reach is the shortest.

# One-liner interview trick

# “Find one island with DFS, then run multi-source BFS from all its cells; first time we touch the other island gives minimum bridge.”  

# Top related problems (same concept)

# Shortest Bridge (LeetCode 934) — basically identical

# Number of Islands (LC 200) — DFS/BFS island detection

# Rotting Oranges (LC 994) — multi-source BFS

# 01 Matrix (LC 542) — multi-source BFS distance

# Nearest Exit from Entrance in Maze (LC 1926) — BFS shortest path

# What was “wrong” (or at least not ideal) in your code
# 1) You keep scanning even after you already found an island

# In your code:

# for r ...
#   for c ...
#     potential_island = traverse_island(...)
#     if len(potential_island) > 0:
#       main_island = potential_island


# Because you don’t break, you continue scanning the whole grid. Since there are exactly two islands, you’ll eventually set main_island to the second island (the last one you encounter in the scan). That still works, but:

# it’s extra work (unnecessary DFS calls),

# and it’s a bit confusing because “main_island” becomes “the last island found”.

# ✅ What I changed: once we find the first island, we break out of the loops immediately.

# 2) You call traverse_island on every cell (including water)

# Your scan calls traverse_island(grid, r, c, set()) even when grid[r][c] == 'W'.

# It still returns empty set quickly, but it’s wasted calls.

# ✅ What I changed: only call DFS when you actually see land:

# if grid[r][c] == 'L':
#     island = traverse_island(...)

# Your question: “Why check L before calling DFS, but inside DFS check W again?”

# Great eye. Two different reasons:

# Reason A: The outer check avoids wasted DFS calls

# Outer check is an optimization:

# If the cell is water, don’t even start DFS.

# Reason B: DFS must still stop when it walks into water

# Inside DFS, you recursively explore neighbors (up/down/left/right).
# Some of those neighbors will be water or out of bounds, so DFS needs a “stop condition”:

# if not inbounds(...) or grid[row][col] == 'W':
#   return visited


# Even if you start from land, DFS will reach water cells around the island edges, so it must handle them.

# So:

# Outer check: “Should I start DFS here at all?”

# Inner check: “While expanding, should I stop expanding from this cell?”

# Both are correct and serve different roles.

# Small note: You pass set() every time — that’s why len(potential_island)>0 works

# Because each DFS call is using a fresh set(), it will either return:

# empty set (if started on water/out of bounds)

# the island cells set (if started on land)

# So your code works, just does more work than needed.

# Bonus: one more micro-improvement

# In your BFS you do:

# if grid[row][col] == 'L' and (row, col) not in main_island:
#   return distance - 1


# This is correct because:

# BFS distance counts steps starting from island land cells (distance 0)

# when you “touch” the other island, the last step is onto land, so flips = distance - 1

# (That -1 is a common point interviewers ask about.)

# Ultra-short brain script:

# “Capture island with DFS → push all island cells into queue → BFS expand → hit second island → return distance-1.”

# 🔥 Final — Pattern Ranking (Important for your brain)

# Difficulty perception:

# 👉 Closest Carrot → BFS only
# 👉 Number of Islands → DFS only
# 👉 Best Bridge → DFS + BFS

# ✅ VERSION 1 — Structured Revision (Corrected + More Precise)
# Pattern Recognition

# Grid + shortest connection between two regions

# 👉 Trigger immediately:

# DFS → identify one island
# Multi-source BFS → shortest expansion to the other

# Approach Steps (Memorize This Flow)
# Step 1 — Find the first island (DFS)

# Scan grid.

# When you see 'L', run DFS.

# Collect all connected land into a set.

# Stop scanning once found.

# ✅ Now you have your starting region.

# Step 2 — Initialize Multi-source BFS

# Push every island cell into the queue with distance 0.

# Mark them visited.

# 👉 BFS is now expanding from the ENTIRE island boundary.

# This guarantees the shortest bridge.

# Step 3 — BFS Expansion Rules (VERY IMPORTANT MEMORY BLOCK)

# Before adding a neighbor to the queue, ALWAYS check:

# ✅ In bounds

# 0 <= row < rows
# 0 <= col < cols


# ✅ Not visited
# (prevents infinite loops)

# ❗ Why I did NOT explicitly check "not water" earlier

# Because in THIS problem:

# 👉 Water is exactly where we WANT to go.

# The bridge is built by flipping water → land.

# So stepping on water is required.

# When do we stop?

# The ONLY cell type we must avoid revisiting is:

# ✅ visited cells.

# We allow both:

# water → expand through it

# land → but only if it's the second island

# Step 4 — Detect the second island

# During BFS:

# if grid[row][col] == 'L'
# and not part of first island:
#     return distance - 1


# ✅ Found shortest bridge.

# Recognition Trigger

# If problem says:

# minimum bridge

# connect islands

# shortest flips

# nearest island

# Your brain should fire instantly:

# 👉 DFS + Multi-source BFS

# This is a HIGH-frequency pattern.

# ✅ VERSION 2 — Ultra Fast Exam Recap (Corrected)
# ⚡ Best Bridge Cheat Sheet

# 👉 DFS one island
# 👉 Push ALL island cells into queue
# 👉 Multi-source BFS through water

# Neighbor rules before enqueue:

# ✔ in bounds
# ✔ not visited

# (Water is allowed — it's the bridge.)

# 👉 First time you touch new land
# → return distance - 1

# One-Line Interview Answer

# “Capture one island with DFS, then run a multi-source BFS expanding through water; the first time we hit the other island gives the minimum bridge.”  