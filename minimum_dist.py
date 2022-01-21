def minimumDistances(a):
    store = []
    for i, x in enumerate(a):
        j = i + 1
        while j < len(a):
            if x == a[j]:
                store.append(abs(i-j))
                break
            j += 1


    if store:
        return min(store)
    else:
        return -1
