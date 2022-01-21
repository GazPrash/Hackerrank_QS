def permutationEquation(p):
    ans = []
    x = 1

    while x <= p:
        for index, num in enumerate(p):
            if num == x:
                ans.append(p.index(index+1))
                x += 1


    return ans