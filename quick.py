
from itertools import count


s = "ABCD"

s1 = "ABA"
s2 = "BB"

# combo = combinations(s, 3)
# s1 = ["".join(_) for _ in combo ]
# print(s1)

s1l = [x for x in s1]
s2l = [x for x in s2]

s1map = set(s1l)
s2map = set(s2l)
counter1 = 0
counter2 = 0   
mark_index = 0
mark_index2 = 0
removed1 = []
removed2 = []
j= 0

for char in s1l:
    if char in s2map:
        removed1.append(char)
        if s2l.index(char) >= mark_index and char not in removed1:  
            mark_index = s2l.index(char)     
            counter1 +=1
        
for char in s2l:
    if char in s1map:
        removed2.append(char)
        if s1l.index(char) >= mark_index2 and char not in removed2:
            mark_index2 = s1l.index(char)     
            counter2 +=1
        

print(counter1, counter2)
print(max(counter1, counter2))