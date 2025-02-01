def avg(a,b,c,d,e):
    aveg=(a+b+c+d+e)/5
    return aveg
def fahr(cel):
    f=(9/5*cel)+32
    return f
def per(l,b):
    per_rect=2*(l+b)
    return per_rect
a=int(input("enter fisrt number:"))
b=int(input("enter second number : "))
c=int(input("enter third number:"))
d=int(input("enter 4th number : "))
e=int(input("enter 5th number : "))
print("Average : " , avg(a,b,c,d,e))
cel=float(input("enter temperature in degree celsius:"))
print("in fahrenheit:", fahr(cel))
l=int(input("enter lenght of rectangle:"))
b=int(input("enter breadth of rectangle:"))
print("perimeter : " , per(l,b))
