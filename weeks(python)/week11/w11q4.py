def search_key_by_value(dictionary, value_to_search):
    # Search through the dictionary and find the key(s) with the given value
    for key, value in dictionary.items():
        if value == value_to_search:
            return key  
    return None 

sample_dict = {
    'apple': 5,
    'banana': 2,
    'cherry': 3,
    'orange': 5,
    'grape': 1
}

value_to_search = int(input("Enter the value to search for: "))
result = search_key_by_value(sample_dict, value_to_search)
if result:
    print(f"The key with the value {value_to_search} is: {result}")
else:
    print(f"No key found with the value {value_to_search}")
