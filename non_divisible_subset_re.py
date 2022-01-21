def nondivisibleset(k, s):
    count = 0
    num_on = None
    
    for x in s:
        if not num_on:
            num_on = x
            
        elif (x%k + num_on%k)%k != 0:
            count += 1
            num_on = x
            
    
    return count