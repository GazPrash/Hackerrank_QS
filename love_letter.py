import string

def love_letter(s):
    if s[::-1] == s:
        return 0

    listed = [x for x in string.ascii_lowercase]
    mark_ind = []
    compare_ind = []

    i = 0
    j = len(s) -1
    while i < len(s)/2:
        pre = listed.index(s[i]) + 1
        post = listed.index(s[j]) + 1
        # print(pre, post)
        if pre != post:
            mark_ind.append(max(pre, post))
            compare_ind.append(min(pre, post))
            

        i += 1
        j -= 1

    x = 0
    diff = 0
    while x < len(compare_ind):
        diff += mark_ind[x] - compare_ind[x]
        x += 1
    
    return diff

love_letter("abcd")  #1234-3-2 1221 abba
        


# print(string.ascii_lowercase)

# for x in string.ascii_lowercase:
#     list.a[dasd]