def countingSort(arr):
    ans = []
    stored = []
    for x in range(len(arr)):
        if x not in stored:
            ans.append(arr.count(x))
            stored.append(x)

    return ans    