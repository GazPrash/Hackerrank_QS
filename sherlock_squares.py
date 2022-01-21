def squares(a, b):
    count = 0
    x = 0
    while True:
        if x**2 > b:
            return count
        elif x**2 < a:
            x += 1
        elif x**2 <= b and x**2 >= a:
            count += 1
            x += 1            
            
    return count 
