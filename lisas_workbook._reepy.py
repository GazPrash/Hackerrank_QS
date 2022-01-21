def repeater(k, arr, ch_no):
    left_overs = arr[i] - k 
    if arr[i] <= ch_no:
        return 1 + repeater(k, arr[i+1], ch_no+1)
    else:
        return repeater(k, arr[i+1], ch_no+1)

def workbook(n, k, arr):
    problems = 0
    #chapters = n
    ch_no = 1
    sp = 0
    
    
    for problems in arr:
        #cringe bruh
        if problems > k:
            left_overs = problems - k
        
        if ch_no in [i for i in range(problems)]:
            sp += 1
            