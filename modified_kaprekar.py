def kaprekarNumbers(p, q):
    answer = []
    for i in range(p, q+1):
        if i == 1:
            answer.append(1)
            
        if len(str(i**2)) == 1:
            continue
        else:
            square = str(i**2)
            a, b = square[:len(square)//2], square[len(square)//2:]
            if int(a) + int(b) == i:
                answer.append(i)

    if answer:
        for x in answer:
            print(x, "", end = "")
    else:
        print("INVALID RANGE")    
