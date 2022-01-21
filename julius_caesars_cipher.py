def caesarCipher(s, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    new_string = []
    for char in s:
        # print(char)
        if char not in alpha:
            #print(char)
            new_string.append(char)
        else:
            old_ind = alpha.index(char.lower())
            new_ind = (old_ind + k)%len(alpha)
            if char.isupper():
                new_string.append(alpha[new_ind].upper())
            else:
                new_string.append(alpha[new_ind])
        
    return ''.join(new_string)
        
