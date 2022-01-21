def closestNumbers(arr):
    arr.sort()
    n = len(arr)
    diff = 0
    diff_list = []
    tup_list = []
    for i, num in enumerate(arr):
        if i < n-1:
            diff = abs(num - arr[i+1])
            if diff_list != []:
                if diff_list[-1] > diff:
                    diff_list.pop()
                    diff_list.append(diff)
                    tup_list = []
                    tup_list.append((num, arr[i+1]))
                elif diff_list[-1] == diff:
                    tup_list.append((num, arr[i+1]))
            else:
                diff_list.append(diff)
                tup_list.append((num, arr[i+1]))

    rt_list = []
    for tupes in tup_list:
        rt_list.append(tupes[0])
        rt_list.append(tupes[1])

    return rt_list

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)

