def gameOfThrones(s):
    n = len(s)
    #set_str = set(s)
    counts = []
        
    if n%2 == 0:
        for x in s:
            if s.count(x)%2 != 0:
                return 'NO'
    else:
        for x in s:
            counts.append(s.count(x))
            
    if len(counts) > n//2:
        return 'NO'
    else:
        mapcount = set(counts)
        for countt in mapcount:
            summ += (countt * counts.count(countt))
            
        if summ == n:
            return 'YES'
        else:
            return 'NO'
        
        
        
    

 
    