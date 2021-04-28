a=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    e=int(input("enter the elements:"))
    a.append(e)
a.sort()
print("the 2nd smallest element is: ",a[1])
