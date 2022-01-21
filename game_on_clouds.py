def jumpingOnClouds(c, k):
    n = len(c)
    jump = (0 + k)%n
    energy = 99

    if c[jump] == 1:
        energy -= 2

    while jump != 0:
        jump = (jump+k)%n
        if c[jump] == 1:
            energy -= 2
        energy -= 1

    return energy