def reverse_words(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

def is_palindrome(input_string):
   
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

def main():
    user_input = input("Enter a long string with multiple words: ")

    reversed_string = reverse_words(user_input)
    
    palindrome_status = is_palindrome(user_input)
    
    print("\nReversed string with words in backward order:")
    print(reversed_string)
    
    if palindrome_status:
        print("\nThe string is a palindrome.")
    else:
        print("\nThe string is not a palindrome.")

main()
