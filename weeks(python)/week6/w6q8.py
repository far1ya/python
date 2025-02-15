def add_numbers_from_list(input_list):
    total = 0
    for item in input_list:
        if isinstance(item, (int, float)):
            total += item
    return total

input_list = [1, 'a', 2, 'b', 3.5, 7, 'c', 4]
result = add_numbers_from_list(input_list)

print("Sum of numbers in the list:", result)
