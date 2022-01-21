def missing(arr, brr):
    notin = []
    setbrr = set(brr)
    setarr = set(arr)

    for x in setbrr:
        if x not in setarr and x not in notin:
            notin.append(x)
        elif x not in notin:
            missing = brr.count(x) - arr.count(x)
            if missing != 0:
                notin.append(x)

    notin.sort()
    return notin



    # for x in brr:
    #     countb.append(brr.count(x))
    
    # for y in arr:
    #     counta.append(arr.count(y))