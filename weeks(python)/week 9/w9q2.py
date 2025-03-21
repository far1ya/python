arr = []
print("Enter 5 integers:")
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    arr.append(num)
print("\nOriginal array:", arr)

reversed_arr = arr[::-1]

print("\nReversed array:", reversed_arr)
