def camelcase(s):
    if s == "":
        return 0

    count  = 1
    for char in s:
        if char.isupper():
            count += 1
            
    return count