def replace(strng):
    char = strng[0]
    length = len(strng)
    strng = strng.replace(char, '$')
    strng = char + strng[1:]
    return strng

print(replace('restart'))
    
    
