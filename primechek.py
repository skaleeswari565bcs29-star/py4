def prime_check(n):
    if n<2:
        return 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input("enter a no:"))
f=0
for i in range(2,n):
    if prime_check(i) and prime_check(n-i):
        print(n,"=",i,"+",(n-1))
        f=1
if not f:
    print("the no cannot be represented by the sum of two prime nos")
