def lexical_order(word_1, word_2, alphabet):
  max_length= max(len(word_1),len(word_2))
  #print(max_length)
  for i in range(0,max_length):
    value_1= alphabet.index(word_1[i]) if i<len(word_1) else float("-inf")
    value_2= alphabet.index(word_2[i]) if i<len(word_2) else float("-inf")
    if value_1<value_2:
      return True
    elif value_2<value_1:
      return False
  return True

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lexical_order("apple", "dock", alphabet)  

# “The loop runs up to the length of the longer word, and inside the loop we do alphabet lookups which are linear in the alphabet size, so overall time complexity is O(n·k).”

# 🧠 Special note (important!)

# If the alphabet is fixed (like English letters, 26):

# k = 26 → constant

# So interviewers often simplify this to:

# O(n)


# But technically, the correct answer is still O(n·k).

# 📦 Space Complexity

# Let’s look at memory usage.

# What extra memory do we use?

# A few variables (max_length, value_1, value_2)

# No extra data structures that grow with input size

# ✅ Space Complexity
# O(1)