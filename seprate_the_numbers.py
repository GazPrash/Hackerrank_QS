def seprate(s): #919293
    num = None
    new_str = ""

    j = 1
    while j < len(s):
        s_dash = s[0:j]
        num = s_dash
        i = 0
        while new_str != s:
            print(new_str) #910
            new_str += str(int(num)+i)
            if i >= 1 and new_str not in s:
                new_str = ""
                break
            i += 1
        if new_str == s:
            print(f"YES {s_dash}")
            return 

        j += 1

    print("NO")
    return



seprate("9910")

                







    
    # if int(s[x(digit-1):2*(digit-1)]) - current != 1:


# a = ["1", "2", "3", "4"]

# num = int("".join(a[:2]))
# print(num)
