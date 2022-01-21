def cutTheSticks(arr):
    now = min(arr)
    sticks = []

    while arr:
        if len(arr) == 1:
            break
        i = 0
        now = min(arr)
        while i < len(arr):
            if arr[i] <= 0:
                arr.remove(arr[i])
            else:
                arr[i] -= now
                
                i += 1
        
        if len(arr) not in sticks and len(arr) != 0:
            sticks.append(len(arr))
                


    return sticks    



cutTheSticks([8, 8, 14, 10, 3 ,5, 14, 12])