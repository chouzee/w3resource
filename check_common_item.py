def common_check(f_list, s_list):
    for el in f_list:
        if el in s_list:
            print(el)


f_list = [1, 2, 3, 4, 5]
s_list = [5, 6, 7, 8, 9]
common_check(f_list,s_list)
