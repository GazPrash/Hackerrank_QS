def anagram(s):
    n = len(s)
    if n%2 != 0:
        return -1
    i = 0
    j = n//2 + i
    countt = 0
    while i < n//2:
        if s[i] != s[j]:
            countt += 1
        
        i += 1
    
    return countt