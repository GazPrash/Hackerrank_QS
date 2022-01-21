def circularArrayRotation(a, k, queries):
    n = len(a)
    i = n - k
    counter = 0

    if n == 1:
        return [0]
    
    if k == 0:
        return [x for x in range(n)]

    k %= n


    vec = []

    while (counter < n):
        vec.append(a[i])
        i = (i+1)%n
        counter += 1

    ans = []

    for q in queries:
        ans.append(vec.index(q))

    return ans




