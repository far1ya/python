str=input("enter String:")
upp=0
low=0
for i in range(0,len(str)):
    if(str[i].isupper()):
        upp=upp+1
    elif(str[i].islower()):
        low=low+1
print("upper : ", upp)
print("lower : ", low)
