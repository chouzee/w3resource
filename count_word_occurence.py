def count_occur(sentence):
    
    occur = dict()
    splitted = sentence.split()
    
    for word in splitted:
        if word in occur:
            occur[word] +=1
        else:
            occur[word] = 1
    return occur

print(count_occur("One one one"))
