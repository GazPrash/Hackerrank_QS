def absolutePermutation(n, k):
    n_listed = [x for x in range(1, n+1)]
    mapped = {}
    ans_list = []

    index = 1
    for num in n_listed:
        while abs(num - (index)) != k:
            index += 1
        
        mapped[index] = num
        index = 1

    sup = sorted(list(mapped.keys()))
    for keys in sup:
        ans_list.append(mapped[keys])

    print(ans_list)

absolutePermutation(3, 2)
        


