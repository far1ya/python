def count_letters(input_string):
    # Create an empty dictionary to store letter counts
    letter_count = {}

    # Loop through each character in the string
    for char in input_string:
        if char.isalpha():  # Ensure we're counting only letters
            char = char.lower()  # Convert to lowercase to count both uppercase and lowercase as the same
            if char in letter_count:
                letter_count[char] += 1  # Increment count if letter is already in dictionary
            else:
                letter_count[char] = 1  # Initialize count for new letter

    return letter_count

# Read input string from the user
input_string = input("Enter a string: ")

# Count letters
result = count_letters(input_string)

# Display the result
print("Letter counts:")
for letter, count in result.items():
    print(f"{letter}: {count}")
