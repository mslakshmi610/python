n=int(input("enter the ilmit"))
a=0
b=1
count=0
if n<0:
    print("enter the positive number")
elif n==1:
    print("fibonacci series upto",n)
    print(a)
else:
    print("fibonacci series are:")
    while count<n:
        print(a)
        sum=a+b
        a=b
        b=sum
        count=count+1