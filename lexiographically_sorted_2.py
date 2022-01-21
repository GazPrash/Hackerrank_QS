def biggerIsGreater(w):
    list_of_w = list(w)

    # LETTERS -> AZCD ->>  AZDC ->> ADZC
    n = len(w)
    i = n - 2
    while i >= 0 and list_of_w[i] > list_of_w[i+1]:
        i -= 1

    if i == -1:
        return "no answer"

    else: 
        j = n - 1
        while j >= 0 and list_of_w[j] <= list_of_w[i]:
            j -= 1

        
        list_of_w[j], list_of_w[i] =  list_of_w[i], list_of_w[j]
        w = "".join(list_of_w)
        ans = w[:i+1] + w[i+1:][::]

        return ans

print(len("gimme_gin_n_tonic"))

print([x for x in range(6)])