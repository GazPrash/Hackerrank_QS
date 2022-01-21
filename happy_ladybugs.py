def happyLadybugs(b):
    # Write your code here'
    bugs = []
    spaces = 0
    for x in b:
        if x != '_':
            y = count(x)
            bugs.append(y)
            if y%2 != 2:
                return 'NO'
        else:
            spaces +=1 
    
    if bugs == []:
        return 'YES'
    
    bugs_unite = False
    for bug in bugs:
        if bug >= 2 and spaces >= 1:
            bugs_unite = True
        else:
            return 'NO'
            
            
    if bugs_unite:
        return 'YES'