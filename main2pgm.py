import set_module
a=map(int,input("enter setA elements:").split())
a=set(a)
b=map(int,input("enter setB elements:").split())
b=set(b)
print("union:",set_module.sunion(a,b))
print("intersection:",set_module.sintersection(a,b))
print("difference:",set_module.sdifference(a,b))
print("symmetric_difference:",set_module.ssymmetricdiff(a,b))
