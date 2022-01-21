
def recursed(wrappers, m, candy):
    if wrappers < m:
        return 0

    candy = wrappers//m
    left = wrappers%m + candy

    return candy + recursed(left, m, candy)


def chocolateFeast(n, c, m):
    candy = n//c
    wrappers = n//c


    return candy + recursed(wrappers, m, candy)
