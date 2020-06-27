def palindrome():
    try:
        num=int(input("enter a number"))
    except  exception as ValueError:
        print("invalid input enter a integer")
    else:
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("the number is palindrome")
        else:
            print("not a palindrome")
    finally:
        print("program executed")
palindrome()