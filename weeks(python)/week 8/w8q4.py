
n = int(input("Enter a number to generate a list of tuples (number, square): "))
result = [(i, i**2) for i in range(1, n+1)]

print("List of tuples (number, square):", result)
