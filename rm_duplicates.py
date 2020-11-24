def rm_duplicates(user_list):
    return set(user_list)

user_list = ['one', 'one', 12, 15, 12]

print(rm_duplicates(user_list))


#another approach through loop iter
# from the solution section

dup_items = set()
uniq_items = []
for a in user_list:
    if a not in dup_items:
        uniq_items.append(a)
        dup_items.add(a)
        
print(dup_items)
