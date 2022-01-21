def strangeCounter(t):
"""
    if t <= 3 and t >= 1:
        return t
        
    if t <= 6 and t > 4:
        return 
"""    
    if t <= 4 and t >=1:
        if t == 4:
            return 6
        
        return 3 -t + 1
    
    x = 1
    k = 0
    store = 0
    
    while x < t:
        store = x
        x = x*2 + 2
        k += 1
    
    if t < 3*(2**k):
        left = t - store
    else:
        left = t - x
    
    return (3 * (2**(k-1)) - left)
        