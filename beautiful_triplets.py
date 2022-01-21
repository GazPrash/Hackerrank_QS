def beautifulTriplets(d, arr):
    triplets = 0
    for i in range(len(arr)):
        if (arr[i] + d) in arr and (arr[i] + 2*d) in arr:
            triplets += 1

    return triplets

beautifulTriplets()
# HERE WE USED THE "IN" FUNCTIONALITY OF PYTHON (CAN USE &&EXISTS() FOR C++) TO FIND OUT THE ITH 
# AND JTH ELEMENT THAT ARE REQUIRED TO FORM THE BEAUTIFUL TRIPLETS. THIS APPROACH IS ALWAYS
# BETTER THAN NAIVELY LOOPING ROW BY ROW OR ELEMENT BY ELEMENT IN ARRAYS.