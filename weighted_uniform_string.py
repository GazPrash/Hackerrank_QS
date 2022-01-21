import string
import math

def customfactorial(x, quo):
    if x == 1:
        return quo
    return x * quo + customfactorial(x-1)  # 2 * 3 + 3 = 9  # Solved Presumably

def uniform(s, queries):
    listed = [x for x in string.ascii_lowercase]
    listed.sort()
    num_list = []
    used = []
    for x in s:
        if x not in used:
            used.append(x)
            num_list.append(customfactorial(s.count(), listed.index(x)+1))
        
    output = []
    for num in queries:
        if num in num_list:
            output.append("Yes")
        else:
            output.append("No")
    
    print(num_list)
    return output

