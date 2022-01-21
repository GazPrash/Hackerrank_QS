def appendAndDelete(s, t, k):
    j = -1
    count = 0
    extra = 0

    if s == t:
        return "Yes"

    while j > -len():
        if s[:j] not in t:
            count += 1
        elif s[:-j] in t and t in s[:-j]:
            count += 1
            break

        elif s[:-j] in t and t not in s[:-j]:
            extra = len(t) - len(s)
            break    


    if k >= 2 * count + extra:
        return "Yes"
    else:
        return "No" 


s = "kasmss"

print(s[:-1])