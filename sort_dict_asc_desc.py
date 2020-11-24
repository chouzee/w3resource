import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sort_by_value(d):
    srt_asc = sorted(d.items(), key=operator.itemgetter(0))
    str_desc = sorted(d.items(), key=operator.itemgetter(0), reverse=True)
    
    print(srt_asc)
    print(str_desc)
    
    
sort_by_value(d)
