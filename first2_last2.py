def first2_last2(strng):
    if len(strng) < 2:
        return "Empty String"
    else:
        f_l = strng[:2] + strng[-2:]
    return f_l
    
    
print(first2_last2("w3resource"))
