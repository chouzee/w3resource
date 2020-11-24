dic={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

def dict_conc(*args):
    dictt = {}
    for i in args:
        dictt.update(i)

    print(dictt)

dict_conc(dic, dic2, dic3)


# another way from solution
dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60}  
dic4 = {}  
for d in (dic1, dic2, dic3): dic4.update(d)  
print(dic4)  
