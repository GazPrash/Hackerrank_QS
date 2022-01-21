def equalizeArray(arr):
    freq = []
    for x in arr:
        freq.append(arr.count(x))

    return len(freq) - max(freq) 
        
