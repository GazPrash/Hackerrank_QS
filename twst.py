def suml(l):
    sum = 0
    for i in l:
       sum = sum + i
    return (sum)

def testque(l,k):
    d = len(l)
    lsum = []

    for i in range(d):
        for j in range(i+1):
            ltemp = l[0+j:d-i+j]
            ltemp2 = l[0 + j:d - i + j]
            lneg = []
            for i in ltemp:
                if i<0:
                    lneg.append(i)
            lneg.sort()
            if len(lneg)<=k:
                for i in lneg:
                    ltemp2.remove(i)
            else:
                for i in range(k):
                    ltemp2.remove(lneg[i])

            print(ltemp2, "ltemp for given r")
        
        lsum.append(suml(ltemp2))
        lsum.sort()

    print(lsum, "this is lsum")
    return (lsum[-1]) 

lis = [2, 3, 2, 2, 5]
testque([6, -5, 3, -7, 6, -1, 10, -8, -8, 8], 2)
