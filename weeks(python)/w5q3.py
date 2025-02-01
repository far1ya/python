string=input("enter a string")
result=" "
for i in range(len(string)):
    if i%2==0:
        result+=string[i]
print("string after removing characters at odd indices: ",result)        
