import math
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiple(a,b):
    return a*b
def division(a,b):
    if b==0:
        return 0
    else:
        return a/b
def modulation(a,b):
    return a%b
def power(a,b):
    return pow(a,b)
def square_root(a):
    return math.sqrt(a)
n1=float(input("enter the first number:"))
n2=float(input("enter the second number:"))
while(1):
    print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.modulation\n6.power\n7.square_root\n8.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        print("addition:",addition(n1,n2))
    elif ch==2:
        print("subtraction:",subtraction(n1,n2))
    elif ch==3:
        print("multiplication:",multiple(n1,n2))
    elif ch==4:
        print("division:",division(n1,n2))
    elif ch==5:
        print("modulation:",modulation(n1,n2))
    elif ch==6:
        print("power:",power(n1,n2))
    elif ch==7:
        print("square_root:",square_root(n1))
    elif ch==8:
        print("exit")
        break
    else:
        print("invalid choice")
