def repl_two_strings(first, last):
    new_first = first[:2] + last[-1]
    new_last = last[:2] + first[-1]
    return new_last + ' ' + new_first


print(repl_two_strings("abc", "xyz"))
