import math

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def calculate_volumes(radius, height, length, width, depth):
    volume_cylinder = math.pi * radius**2 * height
    volume_box = length * width * depth
    return volume_cylinder, volume_box

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_circumference_of_circle(radius):
    return 2 * math.pi * radius

def exchange_values(a, b):
    a, b = b, a
    return a, b

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if __name__ == "__main__":
    # 1. Get input for largest number
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    largest = find_largest(num1, num2, num3)
    print(f"The largest number is: {largest}")

    # 2. Get input for volume calculations
    radius_cylinder = float(input("Enter radius of cylinder: "))
    height_cylinder = float(input("Enter height of cylinder: "))
    length_box = float(input("Enter length of rectangular box: "))
    width_box = float(input("Enter width of rectangular box: "))
    depth_box = float(input("Enter depth of rectangular box: "))
    volume_cylinder, volume_box = calculate_volumes(radius_cylinder, height_cylinder, length_box, width_box, depth_box)
    print(f"Volume of the cylinder: {volume_cylinder}")
    print(f"Volume of the rectangular box: {volume_box}")

    # 3. Get input for rectangle area
    length_rectangle = float(input("Enter length of rectangle: "))
    width_rectangle = float(input("Enter width of rectangle: "))
    area_rectangle = calculate_area_of_rectangle(length_rectangle, width_rectangle)
    print(f"Area of the rectangle: {area_rectangle}")

    # 4. Get input for circumference of circle
    radius_circle = float(input("Enter radius of circle: "))
    circumference = calculate_circumference_of_circle(radius_circle)
    print(f"Circumference of the circle: {circumference}")

    # 5. Get input for exchanging values of two variables
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    a, b = exchange_values(a, b)
    print(f"After exchange: a = {a}, b = {b}")

    # 6. Get input for distance between two points
    x1 = float(input("Enter x1 coordinate: "))
    y1 = float(input("Enter y1 coordinate: "))
    x2 = float(input("Enter x2 coordinate: "))
    y2 = float(input("Enter y2 coordinate: "))
    distance = calculate_distance(x1, y1, x2, y2)
    print(f"Distance between the points: {distance}")
