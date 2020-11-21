def sorted_list(item_list):
    return sorted(item_list, key = lambda x:int(x[-1]))

sr = sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(sr)
