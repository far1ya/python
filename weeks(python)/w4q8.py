n=int(input("enter your number:"))
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
if(c==0):
    print("it is a prime")
else:
    print("it is not a prime")
