import string

# print(string.ascii_lowercase.index('b'))


def swap(string, i, j):
    string = list(string)
    string[i], string[j] = string[j], string[i]
    return "".join(string)


def biggerIsGreater(w):
    mapped_alpha = {}

    for chars in list(string.ascii_lowercase):
        mapped_alpha[chars] = string.ascii_lowercase.index(chars)

    n = len(w)
    i = n - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            if mapped_alpha[w[i]] > mapped_alpha[w[j]]:
                w = swap(w, i, j)
                # print("j: ", j)
                print("before: ", w, j)
                if j >= n - 2:
                    return w
                else:
                    k = n - 1
                    while k > j + 1:
                        l = k - 1
                        print("k: ", k, "\nL: ", l)
                        while l >= j + 1:
                            if mapped_alpha[w[k]] < mapped_alpha[w[l]]:
                                w = swap(w, k, l)

                            l -= 1
                        k -= 1
                    print("after: ", w)
                    return w

            j -= 1

        i -= 1

    return "no answer"

s = "skmidbvygtsdvujmuckkdbceeffrodszmkfrgugelljlxzribxlhltvxgigxfhotkaxejrvymhrengddobeckxhbgxamf"
s =  biggerIsGreater("zxwutljib")
print(s)
