def flatlandSpaceStations(n, c):
    cities = [x for x in range(n)]
    dist = []
    actual_dist = []
     # DONT DO IT WITH BINARY SEARCH JUST O(N2) IS FINE

    for ele in cities:
        low = 0
        high = len(c)-1
        while (low <= high):
            mid = (low+high)//2
            # print(ele, c[mid])
            if ele == c[mid]:
                dist.append(0)
                break
            elif ele < c[mid] and ele > c[mid-1]:
                dist.append(min(abs(ele-c[mid]), abs(ele-c[mid-1])))
                break
            elif ele > c[mid] and ele < c[mid+1]:
                dist.append(min(abs(ele-c[mid]), abs(ele-c[mid+1])))
                break
            elif ele < c[mid]:
                high = mid -1 
            elif ele > c[mid]:
                low = mid+1

        

        actual_dist.append(min(dist))
        dist = []

    print(max(actual_dist)+min(actual_dist), "new answer")
    #return max(actual_dist)


flatlandSpaceStations(6, [0, 1, 2, 3, 4, 5])

# REPS : 0 1 2 3 4    &&   0 4