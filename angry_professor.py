def angryProfessor(k, a):
    count = 0
    for num in a:
        if num <= 0:
            count += 1

    if count >= k:
        print("NO")
    else:
        print("YES")


angryProfessor(9, [13, 91, 56, -62, 96, -5, -84, -36, -46, -13])
