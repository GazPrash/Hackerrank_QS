def activityNotifications(expenditure, d):
    i = 0
    j = d
    n = len(expenditure)
    element_id = d 
    noti = 0
    while j < n-1:
        if d%2 == 0:
            median = (expenditure[(i+j)//2] + expenditure[((i+j)//2) + 1]//2
        else:
            median = expenditure[(i+j)//2]
            
        if expenditure[element_id] >= (2*median):
            noti += 1
            
        i += 1
        j += 1
        element_id += 1
                 
                
    return noti
    
    
    #NOT DONE YET TODO