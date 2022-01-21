def pickingNumbers(a):
    mark = []
    counter = 1
    counter_book = []
    i = 0
    j = 1
    bad_case = False
    while i < len(a):
        print(i, j)
        if j < len(a):
            if abs(a[i] - a[j]) <= 1:
                counter += 1
                if not bad_case:
                    i += 1
                j += 1
            else:
                bad_case = True 
                mark.append(i)
                j += 1
        else:
            counter_book.append(counter)
            if i < len(a):
                bad_case = False
                i = mark[-1]
                j = mark[-1] +1
                counter = 0
            else:
                break


    print(mark)
    return max(mark)

print(pickingNumbers([1, 2, 2, 3, 1, 2]))