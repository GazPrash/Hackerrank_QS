def almostSorted(arr : list):
    i = 0, j = 1
    new = arr[:]
    new2 = arr[:]
    while j < len(arr):
        store = new[i]
        new[i] = new[j]
        new[j] = store
        
        if new == sorted(new):
            print('YES')
            print(f'swap {new[j]} {new[i]}')
            return None
   
    x - len(arr)-1
    
    while x > 0:
        y = 0
        while y < len(arr):
            arr.extend(sorted(new[y:x]))
            if arr == sorted(arr):
                print('YES')
                print(f'reverse {y} {x}')
                return None
                
    print('NO')
    return None