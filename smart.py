def getinput(n):
  l=[]
  for i in range(n):
    i_name = input("enter item name:")
    qua = int(input("enter the quantity:"))
    p = int(input("enter the price:"))
    l.append((i_name, qua, p))
  return l
def subtotal(l):
    s = []
    for i in range(len(l)):
        sub = l[i][1] * l[i][2]
        s.append(sub)
    return s
def total(l):
    t = 0
    for i in range(0, len(s)):
        t = t + s[i]
    print("total:", t)
    if t >= 3000:
        d = t * (10 / 100)
        t = t - d
        print("after discunt:", t)
    else:
        d = 0
        t = t + d
        print("after discunt:", t)
    g = t * (5 / 100)
    t = t + g
    print("GST:", g)
    print("after GST applied:", t)
n = int(input("enter the number of items:"))
r = getinput(n)
print("items:", r)
s = subtotal(r)
print("subtotal:", s)
total(s)
