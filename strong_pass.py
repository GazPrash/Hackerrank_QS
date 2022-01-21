def some(n, password):
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    mage = []
    mage.append(numbers)
    mage.append(lower_case)
    mage.append(upper_case)
    mage.append(special_characters)
    
    add_more = 0
    
    if n < 6:
        add_more += (6-n)
    while mage:
        for char in password:
            for rule in mage:
                if char in rule:
                    mage.remove(rule)
                
    n = len(mage)
    
    return max(add_more, n)
    
