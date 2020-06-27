def max():
    a=int(input("enter num1:"))
    b=int(input("enter num2:"))
    c=int(input("enter num3:"))
    if a==b==c:
        print("all are equal..no maximum number")
    elif (a>b and a>c):
        print("maximum number is:",a)
    elif (b>c and b>a):
        print("maximum number is:",b)
    else:
        print("maximum number is:",c)
max()