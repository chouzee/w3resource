def change_char(strng):
     # We took last char + add items in the middle +
    # add first
    return strng[-1:] + strng[1:-1] + strng[:1]

print(change_char("hello"))

