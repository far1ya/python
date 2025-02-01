def vol(r):
    volm=4/3*(3.14)*(r*r*r)
    return volm
def area(r):
    areaa=3.14*r*r
    return areaa
r=int(input("enter the radius :"))
print("volume:",vol(r))
print("Area:",area(r))
