
n = int(input("How many Fibonacci numbers would you like to generate? "))

a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b 
