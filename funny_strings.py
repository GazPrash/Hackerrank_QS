def funnyString(s):
    ord_keys1 = []
    ord_keys2 = []
    ss = s.reverse()
#    j = len(s) - 1
    for char in s:
        ord_keys1.append(ord(char))

    for char in ss:
        ord_keys2.append(ord(char))
        
        
    ord_keys.sort()
    i = 0
    diff1 = []
    diff2 = []
    #print(ord_keys)
    
    for num in ord_keys1:
        if i != n-1:
            diff1.append(num - ord_keys[i+1])
        i += 1
        
    for num in ord_keys2:
        if i != n-1:
            diff2.append(num - ord_keys[i+1])
        i += 1
        
    i = 0
    diff1.sort()
    diff2.sort()
    
    while i < len(diff1):
        if diff1[i] != diff2[i]:
            return "Not Funny"
            
        i += 1
            
            
    return "Funny"