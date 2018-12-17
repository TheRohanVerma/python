print("enter number for function")
x=int(input("1 for addition or 2 for suntraxtion or 3 for mult or 4 for division")) 
 
def oe():
    if x==1:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a+b)
    elif x==2:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a-b)
    elif x==3:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a*b)
    elif x==4:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a/b)
oe()