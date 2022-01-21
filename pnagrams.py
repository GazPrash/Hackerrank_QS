def pangrams(s):
    for x in s:
        if x not in string.ascii_letters:
            return 'not pangram'
            
    return 'pangram'
    
    
import string

print(string.ascii_letters)