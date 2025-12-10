from collections import Counter
def intersection_with_dupes(a, b):
    counts = {}
    
    # 1. Build the dictionary from B this time
    for item in b:
        counts[item] = counts.get(item, 0) + 1
    
    res = []
    
    # 2. Now iterate through A to check against B's counts
    for item in a:
        if counts.get(item, 0) > 0:
            res.append(item)
            counts[item] -= 1 # Decrease count so we don't over-match duplicates
            
    return res
 

# intersection_with_dupes(
#   ["a", "b", "c", "b"], 
#   ["x", "y", "b", "b"]
# ) # -> ["b", "b"]