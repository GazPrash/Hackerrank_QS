def magic(s):
    i = 0
    sum1 = -1
    sum2 = -1
    sum3 = -1
    # note_num = -1

    sums = []

    while i < 10:
        s[0][0] = i
        for x in s:
            sum1 += x[0]
            sum2 += x[1]
            sum3 += x[2]

        if sum1 == sum2 and sum2 == sum3:
            note_num = i
            sums.append(sum1)

        

        

        


    
        

