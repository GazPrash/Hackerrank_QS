def again(left, k, page, counter, arr):
    page += 1
    left = (left - k)
    problems = [x for x in range(arr[page-1])]
    if page in problems:
        counter += 1

    if left < 0:
        page += 1
    else:
        





def workbook(n, k, arr):
    page = 1
    left = abs(arr[page-1]-k)
    counter = 0
    problems = [x for x in range(arr[page-1])]
    if page in problems:
        counter += 1

    again(left, k, page, counter, arr)

