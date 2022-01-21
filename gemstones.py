def gemstones(arr):
    """
    target = [x for x in arr[0]]
    jooined = ''.join(arr)
    countt = 0
    for char in target:
        if jooined.count(char) == len(arr):
            countt += 1
            
    return countt
    """
    
    rocks = set("".join(arr))
    lastcount = -1
    for word in arr:
        rocks = rocks.intersection(word)
        
    return len(rocks)