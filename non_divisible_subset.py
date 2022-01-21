s = [1, 7, 2, 4]
i = 0
j = 1
count_book = []

mark = s[0]
count = 1
while j < len(s):
    if (s[i] + s[j])%3 != 0:
        count += 1
    else:
        count_book.append(count)
        count = 0

    i += 1
    j += 1


print(max(count_book))

    

