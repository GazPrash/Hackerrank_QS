def alternatingCharacters(s):
    counta = s.count("A")
    countb = s.count("B")
    remove_shit = False

    if countb == counta or abs(counta - countb) == 1:
        if "AA" in s or "BB" in s:
            remove_shit = True
        else:
            return 0

    else:
        remove_shit = True


    store = ""
    dele = 0
    if remove_shit:
        for char in s:
            if store == "":
                store = char
            elif store == char:
                dele += 1
    

    return dele

            
