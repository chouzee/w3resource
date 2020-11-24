def if_empty(user_list):
    if len(user_list) == 0:
        print("The list is empty")
    else:
        print("The list is not empty")

user_list = []

if_empty(user_list)

#from solution section
if not user_list:
    print("List is empty")
