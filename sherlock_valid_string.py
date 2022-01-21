def sherlock_string(s):
    countbook = []
    used = []
    for char in s:
        if char not in used:
            used.append(char)
            countbook.append(s.count(char))
        
    if all(x == countbook[0] for x in countbook):
        return "YES"
        
    # print(countbook)
    # countbook.sort()
    # countbook.reverse()
    
    # countbook[0] -= 1
    
    for num in countbook:
        if 
    
    
    if all(x == countbook[0] for x in countbook):
        return "YES"
    else:
        return "NO"
