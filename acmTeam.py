def acmTeam(topic):
    # NAIVE APPORACH WILL DELYAY IT MORE UPTO; O(N**3) --> USE ZIP FUNC

    countt = 0
    n = len(topic)
    maxx = 0
    double = 1
    
    for i in range(n):
        for bit in range(1, n):
            for x, y in zip(topic[i], topic[bit]):
                if x == 1 or y == 1:
                    countt += 1

            if maxx == countt:
                double += 1
            elif max < countt:
                max = countt 
                countt = 0
    
    return [maxx, double]


# a = "10101"
# b = "01010"
# a = bin(a, 2)
# b = bin(b, 2)
# print(bin(a|b))
