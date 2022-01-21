def ip(s):
    slist = list(s)

    for i in range(6):
        if i%2 != 0:
            slist.insert(i, ".")

    # for x in 

    temp = slist[6:]

    var = int("".join(temp))


    print(var)

ip("2552551135")