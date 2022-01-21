import math


def encryption(s):
    a = "".join(s.split(" "))

    l = math.sqrt(len(a))

    row = math.floor(l)
    col = math.ceil(l)

    res = ""
    for i in range(col):
        res += f"{a[i::col]} "

    print(res[:-1])


encryption("feedthedog")
