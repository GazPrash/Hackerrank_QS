def repeatedString(s, n):
    ratio = n%len(s)

    # if s == "a":
    #     return n

    # if len(s) > n:
    #     ans =  s[0:len(s)-n]

    # else:
    #     a = n//len(s)
    #     countt = s.count("a")
    #     countt *= a

    # if ratio != 0:
    #     countt += s[:n%len(s)].count("a")

    print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

repeatedString("aab", 882787)