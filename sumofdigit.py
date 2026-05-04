def sum(n,s=0):
    if n==0:
        return 0
    else:
        rem=n%10
        s=s+rem
        return s+sum(int(n/10))
n=int(input("enter a no:"))
print("sum of digits:",sum(n))
