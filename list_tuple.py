lists=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    e=int(input("enter the elements:"))
    lists.append(e)
print(lists)
tuples=tuple(lists)
print(tuples)