def intersection_with_dupes(a, b):
    # Optimization: ensure 'a' is the smaller list to save memory on the dictionary
    if len(a) > len(b):
        a, b = b, a
        
    counts = {}
    # Count frequency of the first list
    for item in a:
        counts[item] = counts.get(item, 0) + 1
    
    res = []
    # Check second list against the counts
    for item in b:
        if counts.get(item, 0) > 0:
            res.append(item)
            counts[item] -= 1 # Decrement to ensure we handle duplicates correctly
            
    return res