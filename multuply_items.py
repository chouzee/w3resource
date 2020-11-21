def list_sum(item_list):
    total = 1
    for i in item_list: 
        total *= i 
    return total
print(list_sum([1, 2, 3]))
