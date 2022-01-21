def pairs(k, arr):
    # O(n^2) soln, pretty bad obv...
    pairs = 0
    for index, item in enumerate(arr):
        for ele in (arr[index+1:]):
            if abs(item - ele) == k:
                print(item, ele)
                pairs += 1

    return pairs

    # *cheating* solution ---> just sort

def pairs(k ,arr):
    arr.sort()
    pairs = 0
    i, j = 0, 0

    while j < len(arr):
        d = arr[j] - arr[i]

        if d == k:
            pairs += 1
            j+= 1

        elif d > k:
            i+= 1

        elif d < k:
            j += 1

    return pairs