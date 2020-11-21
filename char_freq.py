def char_count(calc_str):
    dict = {}
    for i in calc_str:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(char_count("google.com"))
