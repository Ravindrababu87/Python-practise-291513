tuple=(4,5,7,1,14,4,6,4,9,6,4,6,4)
for i in tuple:
    if tuple.count(i)>1:
        print(i,"is repeated",tuple.count(i),"times")