def timeinWords(h, m): 
    refer = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
    }


    # IF-ELSE LADDER ~~

    if m == 0:
        return f"{refer[h]} o' clock"
    
    elif m == 1:
        return f"{refer[m]} minute past {refer[h]}"

    elif m > 0 and m < 15:
        return f"{refer[m]} minutes past {refer[h]}"
    
    elif m == 15:
        return f"quarter past {refer[h]}"

    elif m > 15 and m <= 20:
        return f"{refer[m]} minutes past {refer[h]}"
    
    elif m > 20 and m < 30:
        return f"{refer[20]} {refer[m-20]} minutes past {refer[h]}"

    elif m == 30:
        return f"half past {refer[h]}"

    elif m > 30 and m < 40:
        x = 60 - m
        return f"{refer[20]} {refer[x-20]} minutes to {refer[h+1]}"

    elif m > 40 and m < 45:
        return f"{refer[60 - m]} minutes to {refer[h+1]}"

    elif m == 45:
        return f"quarter to {refer[h+1]}"

    elif m > 45:
        return f"{refer[60 - m]} minutes to {refer[h+1]}"

print(timeinWords(1, 1))
