def recursed(list1, list2, i, markindices):
    if i >= len(list1):
        return markindices
    
    elif list1[i] in list2:
        markindices.append(list2.index(list1[i]))

        return recursed(list1, list2, i+1, markindices)
    
    else:
        return []



def checkInclusion(s1, s2):
    if s1 in s2:
        return True

    if len(s1) > len(s2):
        return False

    s1l = [x for x in s1] 
    s2l = [x for x in s2]

    markindices = []
    ans = recursed(s1l, s2l, 0, markindices)
    if not ans:
        return False
    else:
        ans.sort()
        ok = False
        index = 1
        for x in ans:
            if index != len(ans):
                if abs(x - ans[index]) == 1:
                    ok = True
                else:
                        ok = False
            index +=1

    return ok


checkInclusion("ab", "ebaooo")