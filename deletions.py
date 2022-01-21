def makingAnagrams(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    same = 0
    for ele in set1.intersection(set2):
        min_occ = min(s1.count(ele), s2.count(ele))

        same += 2*min_occ

    return len(s1) + len(s2) - same
