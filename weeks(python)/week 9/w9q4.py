n = int(input("Enter the number of elements in the list: "))
arr = []
print(f"Enter {n} numbers:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    arr.append(num)

total_sum = sum(arr)
average = total_sum / n
print(f"\nThe average of the numbers in the list is: {average}")
