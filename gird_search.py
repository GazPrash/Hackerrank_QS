def gridSearch(G, P):
    index = 0
    n = len(P)
    last_ind = -1
    removed = 0    
    for stuff in G:
        if index < n:
            print(P[index], stuff)
            if P[index] in stuff:
                print(index)
                if last_ind == -1:
                    last_ind = index
                elif abs(last_ind - index) == 1:
                    return "NO"
                else:
                    last_ind = index
                    
                removed += 1                
                index += 1
        
    print(P, removed)
    if removed == n:
        return "YES"
    else:
        return "NO"
