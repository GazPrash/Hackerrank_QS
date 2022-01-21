import math

def strangeCounter(t):
    """
    y = 0
    parameter = 3 * (2**(y)) ---> logic ---> so y becomes log2(t/3)
    while t//(parameter)) != 1:
        y += 1
    
    
    parameter - 
    """
    multi = 3
    while t > multi:
        t = t - multi
        multi*= multi
        
    return multi -t + 1
    
 
    
    
    
    