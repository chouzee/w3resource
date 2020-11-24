def change_char(strng):
    return strng[-1:] + strng[1:-1] + strng[:1]

print(change_char("hello"))

