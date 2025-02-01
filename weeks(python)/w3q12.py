n=int(input("enter number:"))
c=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        c=c+1
        print("first factor: ", i)
        break
if(c==0):
    print("is prime")
    print("first factor is : 1")
else:
    print("not a prime")
