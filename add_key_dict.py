def add(key, value):
    d = {0: 10, 1: 20}
    d[key] = value
    return d
    
add(3, 30)

#there is much easy way from Solution
d = {0:10, 1:20}  
print(d)  
d.update({2:30})  
print(d)

