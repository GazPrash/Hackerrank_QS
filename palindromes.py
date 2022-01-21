def palindromeIndex(s):
    strr = list(s)
    n = len(strr) -1

    if n+1 == 2:
        if strr[0] == strr[1]:
                return -1
    elif (n+1)%2 != 0:
            if strr[:(n+1)//2] == (strr[(n+1)//2 + 1:][::-1]):
                return -1
    else:
        if strr[:(n+1)//2] == (strr[(n+1)//2:][::-1]):
            return -1

    for i, char in enumerate(strr):
        new = strr[::]

        del new[i]
        if n == 2:
            if new[0] == new[1]:
                return i
        elif n%2 != 0:
            if new[:n//2] == (new[n//2 + 1:][::-1]):
                return i

        else:
            if new[:n//2] == (new[n//2:][::-1]):
                return i

        del new

    return -1


#  1 2 3 4 5 6 7 8 

print(palindromeIndex("123454321"))