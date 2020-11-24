user_input = "Hello"

def check_input(user_input):
    if isinstance(user_input, str):
        return True
    else:
        return False
    
print(check_input(user_input))
