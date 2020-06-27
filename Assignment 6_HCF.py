def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=y
        for i in range(1,smaller+1):
            if((x%i==0) and (y%i==0)):
                hcf=1
        return hcf
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print("the H.C.F. of",num1,"and",num2,"is",hcf(num1,num2))