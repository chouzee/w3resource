def not_and_poor(str1):
    nott = str1.find("not")
    bad = str1.find("poor")
    if nott > bad:
        str1 = str1.replace(str1[nott:(bad+4)], 'good')
    return str1
print(not_and_poor("The lyrics is not that poor!"))
