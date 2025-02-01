import math
n=int(input("enter number:"))
x1=(5*n*n)+4
x2=(5*n*n)-4
s1=int(math.isqrt(x1))
s2=int(math.isqrt(x2))
if(s1**2==x1 or s2**2==x2):
    print("is fibbonacci number")
else:
    print("not fibonacci")
