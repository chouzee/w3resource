def replace(strng):
    char = strng[0]
    # replace all occurences
    strng = strng.replace(char, '$')
    # it missed first r since we used +
    strng = char + strng[1:]
    return strng

print(replace('restart'))
