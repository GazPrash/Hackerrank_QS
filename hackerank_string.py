def hackerrankInString(s):
    we_have = "hackerrank"
    iter = 0

    for char in s:
        if char == we_have[iter]:
            if iter == len(we_have) -1:
                return "YES"
            iter += 1
                
    return "NO"