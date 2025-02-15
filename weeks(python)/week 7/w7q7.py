
numbers = [int(x) for x in input("Enter the numbers separated by spaces: ").split()]

numbers.sort(reverse=True)

for num in numbers:
    if num != numbers[0]:
        second_largest = num
        break

print(f"The second largest number is {second_largest}.")
