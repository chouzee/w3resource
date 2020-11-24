lst = [1, 2, 3]

def copy_list(lst):
    new_list = lst[:]
    return new_list

print(copy_list(lst))


# solution section
original_list = [10, 22, 44, 23, 4]  
new_list = list(original_list)  
print(original_list)  
print(new_list)  
