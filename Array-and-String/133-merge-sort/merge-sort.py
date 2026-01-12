from collections import deque
def merge_sort(nums):
  if len(nums)<=1:
    return nums
  mid= len(nums)//2
  left_sorted= merge_sort(nums[:mid])
  right_sorted= merge_sort(nums[mid:])
  return merge(left_sorted,right_sorted)
  
def merge(list_1,list_2):
  merge=[]
  list_1= deque(list_1)
  list_2= deque(list_2)
  while list_1 and list_2:
    if list_1[0]<list_2[0]:
      merge.append(list_1.popleft())
    else:
      merge.append(list_2.popleft())
  merge+=list_1
  merge+=list_2
  return merge
  





# “Merge Sort divides the list into halves log n times, and at each level it merges all n elements, so the time complexity is O(n log n).”
# “Merge Sort needs extra memory to store merged arrays, so its space complexity is O(n).”
# If interviewer asks:

# “Why would you still use Merge Sort if it uses extra memory?”

# Answer:

# “Because Merge Sort guarantees O(n log n) time even in the worst case and is stable, which makes it useful for large datasets and linked lists.”

# 🧩 Final ultra-simple summary (memorize this)

# Time: O(n log n) → split log n times, merge n each time

# Space: O(n) → needs extra memory to merge

# Ordering from fastest to slowest (important for interviews)
# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n²)
# O(2ⁿ)

# We’ll use:

# numbers = [4, 2, 5, 1]

# 🔁 YOUR CODE (unchanged)
# def merge_sort(nums):
#   if len(nums) <= 1:
#     return nums  

#   mid_idx = len(nums) // 2
#   left_sorted = merge_sort(nums[:mid_idx])
#   right_sorted = merge_sort(nums[mid_idx:])  

#   return merge(left_sorted, right_sorted)

# 🧠 Rule to remember while reading

# Python does NOT move to the next line until the current line finishes completely.

# So this line:

# left_sorted = merge_sort(nums[:mid_idx])


# 👉 must finish fully before right_sorted starts.

# STEP 1: First call
# merge_sort([4, 2, 5, 1])


# len(nums) = 4 → not base case

# mid_idx = 2

# Splits into:

# nums[:2] = [4, 2]
# nums[2:] = [5, 1]


# Python now executes:

# left_sorted = merge_sort([4, 2])


# ⏸️ Everything else is PAUSED.

# STEP 2: Sorting LEFT part
# merge_sort([4, 2])


# length = 2 → not base case

# mid_idx = 1

# Splits into:

# [4] and [2]


# Python executes:

# left_sorted = merge_sort([4])

# STEP 3: Base case hit ✅
# merge_sort([4])


# length = 1

# returns immediately:

# return [4]


# So now:

# left_sorted = [4]

# STEP 4: Sort RIGHT of [4,2]

# Python now runs the next line:

# right_sorted = merge_sort([2])


# base case

# returns [2]

# Now we have:

# left_sorted  = [4]
# right_sorted = [2]

# STEP 5: FIRST MERGE (inside [4,2])
# return merge([4], [2])


# Merge result:

# [2, 4]


# So:

# merge_sort([4,2]) → [2,4]


# This value is returned to the first call.

# STEP 6: Back to FIRST call

# We now resume:

# merge_sort([4,2,5,1])


# We already finished:

# left_sorted = [2, 4]


# Now Python runs:

# right_sorted = merge_sort([5, 1])

# STEP 7: Sorting RIGHT part
# merge_sort([5, 1])


# split into [5] and [1]

# left_sorted = merge_sort([5]) → [5]
# right_sorted = merge_sort([1]) → [1]

# STEP 8: SECOND MERGE (inside [5,1])
# return merge([5], [1])


# Result:

# [1, 5]


# So:

# merge_sort([5,1]) → [1,5]

# STEP 9: FINAL MERGE 🔥🔥

# We are back to the very first call:

# left_sorted  = [2, 4]
# right_sorted = [1, 5]


# Python now executes:

# return merge([2, 4], [1, 5])


# Merging step-by-step:

# compare 2 & 1 → take 1

# compare 2 & 5 → take 2

# compare 4 & 5 → take 4

# append leftover 5

# Result:

# [1, 2, 4, 5]

# ✅ FINAL OUTPUT
# merge_sort([4, 2, 5, 1])
# → [1, 2, 4, 5]

# 🧩 WHY THIS FINALLY WORKS (IMPORTANT)
# 🔽 Going DOWN (splitting)
# [4,2,5,1]
# → [4,2] [5,1]
# → [4] [2] [5] [1]

# 🔼 Coming UP (merging)
# [4] + [2] → [2,4]
# [5] + [1] → [1,5]
# [2,4] + [1,5] → [1,2,4,5]

# 🧠 ONE LAST MENTAL MODEL (very important)

# Each merge_sort call waits until both left_sorted and right_sorted are returned.

# Nothing is merged early.
# Everything merges only while returning back up.

# Now let’s lock it in with 5 values, using your exact code, same variable names, same flow, and no shortcuts.

# We’ll use:

# numbers = [7, 3, 5, 2, 4]

# 🔁 YOUR EXACT CODE (unchanged)
# def merge_sort(nums):
#   if len(nums) <= 1:
#     return nums  

#   mid_idx = len(nums) // 2
#   left_sorted = merge_sort(nums[:mid_idx])
#   right_sorted = merge_sort(nums[mid_idx:])  

#   return merge(left_sorted, right_sorted)

# 🧠 Rule to keep in mind (read this first)

# Python finishes one function call completely before going back to the previous one.
# Every merge_sort call waits until its children finish.

# STEP 1: First call
# merge_sort([7, 3, 5, 2, 4])


# length = 5 → not base case

# mid_idx = 5 // 2 = 2

# Split into:

# nums[:2]  = [7, 3]
# nums[2:]  = [5, 2, 4]


# Python runs:

# left_sorted = merge_sort([7, 3])


# Everything else is paused.

# STEP 2: Sorting LEFT [7, 3]
# merge_sort([7, 3])


# length = 2

# mid_idx = 1

# Split:

# [7] and [3]

# STEP 2.1
# left_sorted = merge_sort([7]) → [7]

# STEP 2.2
# right_sorted = merge_sort([3]) → [3]

# STEP 2.3 — FIRST MERGE
# return merge([7], [3]) → [3, 7]


# So:

# merge_sort([7,3]) → [3,7]


# Returned to first call.

# STEP 3: Back to FIRST call

# Now we have:

# left_sorted = [3, 7]


# Python runs:

# right_sorted = merge_sort([5, 2, 4])

# STEP 4: Sorting RIGHT [5, 2, 4]
# merge_sort([5, 2, 4])


# length = 3

# mid_idx = 1

# Split:

# [5] and [2, 4]

# STEP 4.1: Sort [5]
# merge_sort([5]) → [5]

# STEP 4.2: Sort [2, 4]
# merge_sort([2, 4])


# length = 2

# split into [2] and [4]

# merge_sort([2]) → [2]
# merge_sort([4]) → [4]

# STEP 4.2.1 — MERGE
# merge([2], [4]) → [2, 4]


# So:

# merge_sort([2,4]) → [2,4]

# STEP 4.3 — MERGE [5] and [2,4]

# Now:

# left_sorted  = [5]
# right_sorted = [2, 4]

# return merge([5], [2,4]) → [2, 4, 5]


# So:

# merge_sort([5,2,4]) → [2,4,5]


# Returned to first call.

# STEP 5: FINAL MERGE 🔥🔥🔥

# We are back at:

# merge_sort([7,3,5,2,4])


# Now we have:

# left_sorted  = [3, 7]
# right_sorted = [2, 4, 5]


# Python executes:

# return merge([3,7], [2,4,5])


# Merging step-by-step:

# compare 3 & 2 → take 2

# compare 3 & 4 → take 3

# compare 7 & 4 → take 4

# compare 7 & 5 → take 5

# append leftover 7

# Result:

# [2, 3, 4, 5, 7]

# ✅ FINAL OUTPUT
# merge_sort([7, 3, 5, 2, 4])
# → [2, 3, 4, 5, 7]

# 🧩 VISUAL SUMMARY (THIS IS THE “AHA” PART)
# 🔽 SPLITTING (going down)
# [7,3,5,2,4]
# → [7,3]     [5,2,4]
# → [7] [3]   [5] [2,4]
# →            [2] [4]

# 🔼 MERGING (coming up)
# [7] + [3]     → [3,7]
# [2] + [4]     → [2,4]
# [5] + [2,4]   → [2,4,5]
# [3,7] + [2,4,5] → [2,3,4,5,7]

# 🧠 FINAL MENTAL MODEL (lock this in)

# Recursion goes down until it cannot split anymore,
# then merges while returning back up.

# If this version made sense, you’ve officially understood recursion + merge sort 🎉
  