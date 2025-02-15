import math

def triangle_type_and_area(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        s = (a + b + c) / 2 
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        if a == b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"
        
        return area, triangle_type
    else:
        return None, "Invalid triangle sides"

a = float(input("Enter the first side length of the triangle: "))
b = float(input("Enter the second side length of the triangle: "))
c = float(input("Enter the third side length of the triangle: "))

area, triangle_type = triangle_type_and_area(a, b, c)

if area is None:
    print(triangle_type)  
else:
    print(f"The area of the triangle is: {area:.2f}")
    print(f"The triangle is {triangle_type}.")
