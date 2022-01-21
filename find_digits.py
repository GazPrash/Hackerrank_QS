def findDigits(n):
    str_num = str(n)
    count = 0
    for digit in str_num:
        if int(digit) != 0 and n%int(digit) == 0:
            count += 1

    return count