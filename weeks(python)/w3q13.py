a=int(input("enter fisrt number:"))
b=int(input("enter second number : "))
while(b!=0):
    a=b
    b=a%b
print("GCD=", a)
