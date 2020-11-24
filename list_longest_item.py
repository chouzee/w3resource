def long_words(n, strng):
    w_len = []
    splitted = strng.split()
    for i in splitted:
        if len(i) > n:
            w_len.append(i)
    return w_len
    


print(long_words(3, "The quick brown fox jumps over the lazy dog"))  
