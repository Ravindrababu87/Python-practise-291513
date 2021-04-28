a=[]
n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    e=int(input("enter the elements:"))
    a.append(e)
a.sort()
print("The sorted list is:",a)
    k=a[n]
    a[n]=a[n+1]
    a[n+1]=k
print("the changed lis is: ",a)
