def decompress_braces(string):
  stack=[]
  nums="123456789"
  for ch in string:
    if ch in nums:
      stack.append(int(ch))
    else:
      if ch=="}":
        segment=''
        while isinstance(stack[-1],str):
          popped= stack.pop()
          segment= popped+segment
        num= stack.pop()
        stack.append(segment*num)
      elif ch!="{":
        stack.append(ch)
  return ''.join(stack)


# s = length of string
# m = count of brace pairs
# Time: O((9^m) * s)
# Space: O((9^m) * s)





# Correct way to think about complexity

# The big cost is output size.

# Let:

# s = length of input string

# L = length of the decompressed output (can be huge)

# Then:

# ✅ Time: O(s + L)
# ✅ Space: O(s + L) (stack + output)

# Why?
# Because you must actually build the output, which takes L work. No algorithm can do better than O(L) if it must return the full string.

# Your 9^m idea is trying to describe worst-case growth if each brace repeats up to 9 and nesting depth is m. That growth is real, but the clean interview statement is:

# “Time and space are linear in the size of the output.”

# If they want worst-case growth, you can add:

# “In worst-case nested repetition, output can grow exponentially with nesting depth.”

# Small issues / improvements in your code
# 1) Only supports digits 1–9 (single digit)

# You used:

# nums = "123456789"


# So "12{a}" won’t work.

# 2) Type-mixing in stack works, but you must ensure stack top is always valid

# You do:

# while isinstance(stack[-1], str):


# That’s fine if the stack is well-formed, but in malformed input it can error. (Problem usually guarantees valid encoding.)

# 3) Efficiency improvement (optional)

# Building segment by string concatenation in a loop can be slightly slower. You can build a list and reverse/join, but it’s usually okay.

# Interview-ready improved version (handles multi-digit counts)
# def decompress_braces(string):
#     stack = []
#     num = 0

#     for ch in string:
#         if ch.isdigit():
#             # build multi-digit number: "12" -> 12
#             num = num * 10 + int(ch)

#         elif ch == "{":
#             # push the number and a marker, reset num
#             stack.append(num)
#             stack.append("{")
#             num = 0

#         elif ch == "}":
#             # pop characters until "{"
#             segment_parts = []
#             while stack[-1] != "{":
#                 segment_parts.append(stack.pop())
#             stack.pop()          # remove "{"
#             k = stack.pop()      # repetition count

#             segment = "".join(reversed(segment_parts))
#             stack.append(segment * k)

#         else:
#             # normal letter
#             stack.append(ch)

#     return "".join(stack)

# Complexity (best statement)

# Time: O(s + L)

# Space: O(s + L)
# Where L is decompressed output length.

# Is there a “better” asymptotic way?

# Not if you must return the full decompressed string. Returning a huge string inherently costs huge time + memory.

# The only way to “beat” that is if the problem allowed returning a lazy iterator / generator or a compressed representation — but this problem returns the full string.

# If you share 1–2 sample inputs you’re testing (especially nested ones), I can walk through the stack state step-by-step like we did earlier.

# did'nt get  for ch in string:
#         if ch.isdigit():
#             # build multi-digit number: "12" -> 12
#             num = num * 10 + int(ch)  show with one digit and muti digit example

# Perfect question 👍
# This line is very important, so let’s explain it slowly with numbers, first single-digit, then multi-digit.

# The line in question
# num = num * 10 + int(ch)

# What is num?

# num is the number we are building while reading digits

# We read digits one character at a time

# 1️⃣ Single-digit example
# Input
# "3{a}"

# Step by step

# Initial:

# num = 0


# Read '3':

# num = num * 10 + int('3')
# num = 0 * 10 + 3
# num = 3


# ✅ Correct — num becomes 3

# Then { appears → we use num = 3 as the repeat count.

# 2️⃣ Multi-digit example (THIS is the key)
# Input
# "12{a}"


# Characters are read one by one:

# '1' → '2' → '{'

# Step-by-step walkthrough

# Initial:

# num = 0

# Read '1'
# num = num * 10 + int('1')
# num = 0 * 10 + 1
# num = 1


# So far:

# num = 1

# Read '2'
# num = num * 10 + int('2')
# num = 1 * 10 + 2
# num = 12


# So now:

# num = 12

# Read '{'

# Now we know the full number is finished.

# We push 12 to the stack and reset:

# stack.append(12)
# num = 0

# Why multiply by 10?

# Because of place value.

# Think how numbers work:

# Digits	Math
# "3"	3
# "12"	1×10 + 2
# "345"	3×100 + 4×10 + 5

# This line simulates that process digit by digit.

# 3️⃣ Bigger multi-digit example
# Input
# "345{ab}"


# Steps:

# ch	calculation	num
# '3'	0*10+3	3
# '4'	3*10+4	34
# '5'	34*10+5	345
# '{'	use 345	reset
# 4️⃣ Why your old code couldn’t do this

# Your original version had:

# if ch in "123456789":
#     stack.append(int(ch))


# So "12{a}" became:

# 1, 2   ❌ (two separate numbers)


# Instead of:

# 12     ✅ (one number)

# Mental rule to remember (VERY IMPORTANT)

# If digits can be more than one character, always build the number using
# num = num * 10 + digit

# One-line interview explanation

# “I build multi-digit numbers incrementally using place value as I scan the string.”

# If you want next, I can:

# Trace "3{a2{bc}}" fully with stack states

# Or show why num = num * 10 + int(ch) works for any base-10 number

# why the time and space not similar to uncompress problem i done just before. it looks similar

# They are similar — the difference is what controls the work.

# Both problems ultimately depend on how big the output becomes.
# That’s why the clean complexity for both is:

# Time: O(input length + output length)
# Space: O(output length) (plus small helpers)

# So if they look different, it’s mostly just how we describe output size.

# 1) Your earlier uncompress (like "2c3a1t")

# Output length is predictable:

# Suppose there are n groups

# Each group repeats up to m times
# Then output length L ≈ n * m

# So people write:

# Time: O(n * m)

# Space: O(n * m)

# This is just a different way of saying:

# Time: O(s + L) where L = n*m

# Space: O(L)

# 2) Brace decompress (like "3{a2{bc}}")

# Here, repeats can be nested, so output can explode:

# Example:

# 9{9{9{a}}} → output length is 9 * 9 * 9 = 729

# So we describe it as:

# Time: O(s + L)

# Space: O(L)

# Because L can be exponential in nesting depth, and using L keeps the statement accurate without guessing a formula.

# Your 9^m comment is basically trying to express “L can blow up”, and it’s not wrong as an intuition — it’s just not the best interview phrasing.

# 3) Why they look different (the real reason)

# In simple uncompress, growth is “flat”: groups repeat independently → L ~ n*m

# In brace decompress, growth can be “nested”: repeats multiply → L can be huge

# But the unified truth is:

# ✅ Both are O(s + L) time and O(L) space
# Where L is the length of the final decompressed string.

# Interview-ready way to say it
# For uncompress

# “Time and space are linear in the output size. Since output is about nm, it’s O(nm).”

# For brace decompress

# “Time and space are linear in the output size, which can grow exponentially with nesting.”

# If you want, give me one brace input you find confusing (like 2{ab3{c}}) and I’ll compute its L and show exactly how that drives runtime.

# in short

# In short:

# They are the same pattern.

# Both problems run in time proportional to the output size.

# Both use space proportional to the output size.

# Why they look different:

# In simple uncompress, output grows like n × m, so people write O(nm).

# In brace decompress, output can grow nested/exponentially, so we write O(s + L).

# Unified rule (remember this):

# Any decompression problem is O(input + output).

# That’s the clean interview answer.

# write again time and space for both in short

# Sure — here it is very short and clear, side-by-side.

# Uncompress (e.g. "2c3a1t")

# Time: O(L)

# Space: O(L)

# L = length of decompressed output (≈ n × m)

# Decompress with braces (e.g. "3{a2{bc}}")

# Time: O(L)

# Space: O(L)

# L = length of decompressed output (can grow exponentially with nesting)

# One rule to remember

# Decompression problems always take time and space proportional to the output size.


# LeetCode equivalents

# Decode String (LeetCode 394) → Medium

# Very close (same pattern, same difficulty)

# Decode String — LeetCode 394 (Medium)

# "3[a2[c]]" → "accaccacc"

# Stack + parsing + nesting

# This is the canonical version of your problem

# String Decompression / Uncompress — (Structy / AlgoExpert)

# "2c3a1t" → "ccaaat"

# Same idea, no nesting

# 🔹 Same pattern family (stack + parsing)

# Basic Calculator II — LeetCode 227 (Medium)

# Parse numbers and operators

# Stack + multi-digit parsing

# Mini Parser — LeetCode 385 (Medium)

# Parse nested lists like "[123,[456,[789]]]"

# Very similar stack logic

# Count and Say — LeetCode 38 (Medium)

# Run-length encoding / decoding

# Group parsing

# 🔹 Easier but related

# String Compression — LeetCode 443 (Medium)

# Compress groups of characters

# Two-pointer grouping

# 🔑 One-line memory rule

# If the problem has numbers + characters + nesting, think stack + parsing.
