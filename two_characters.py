def alternate(s):
    setthem = set(s)
    freq = []
    alpha = []
    removed = []
    n = len(setthem)
    
    
    for char in setthem:
        freq.append(s.count(char))
        alpha.append(char)
        
    last_ch = ""
    for ch in s:
        if last_ch == "":
            last_ch = ch
        elif last_ch == ch:
            alpha.remove(ch)
            freq.remove(alpha.index(ch))


    freq.sort()
    for index, num in enumerate(freq):
        if abs(num - freq[index+1]) == 1:
            return (num + freq[index+1])
            
        