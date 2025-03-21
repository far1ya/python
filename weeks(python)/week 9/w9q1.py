arr = []
print("Enter 5 integers:")
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    arr.append(num)

print("\nThe entire array:", arr)
for i in range(5):
    print(f"Element at index {i}: {arr[i]}")
