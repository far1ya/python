
numbers = [int(x) for x in input("Enter the numbers separated by spaces: ").split()]
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

if n > 1:
    second_largest = numbers[-2]
    print(f"The second largest number is: {second_largest}")
else:
    print("There is no second largest number.")
