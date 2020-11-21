def number_count(item_list):
    count = 0
    for i in item_list:
        if i[0] == i[-1]:
            count += 1
    print(count)
    
number_count(['abc', 'xyz', 'aba', '1221', 'zyz'])
