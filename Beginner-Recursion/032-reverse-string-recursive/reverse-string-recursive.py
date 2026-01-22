def reverse_string(s):
    # Base case:
    # If the string is empty, there is nothing to reverse
    if len(s) == 0:
        return ""
    
    # Recursive case:
    # 1. Reverse the substring excluding the first character
    # 2. Append the first character at the end
    return reverse_string(s[1:]) + s[0]

# Example:
# reverse_string("hello")
# -> reverse_string("ello") + "h"
# -> reverse_string("llo") + "e" + "h"
# -> reverse_string("lo") + "l" + "e" + "h"
# -> reverse_string("o") + "l" + "l" + "e" + "h"
# -> "" + "o" + "l" + "l" + "e" + "h"
# -> "olleh"

# One-line explanation to say in interview

# “I use recursion by defining a base case for an empty string, then reverse the remaining substring and append the first character at the end.”