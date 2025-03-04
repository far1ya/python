input_string = input("Enter a string: ")
if len(input_string) < 2:
    result = ""
else:
    result = input_string[:2] + input_string[-2:]
print("Result:", result)
