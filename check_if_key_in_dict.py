dic={1:10, 2:20}


def check_key(key):
    if key in dic:
        print(f"The key {key} is in the dict")
    else:
        print(f"The key {key} does not exist")

check_key(3)
