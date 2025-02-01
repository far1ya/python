text=input("enter a text")
vowels = "aeiouAEIOU"  
vowel_count = 0
vowel_list = []

for char in text:
    if char in vowels:
        vowel_count += 1
        vowel_list.append(char)

print(f"Total number of vowels: {vowel_count}")
print(f"Vowels in the text: {vowel_list}")
