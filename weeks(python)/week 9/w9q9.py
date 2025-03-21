dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}


merged_dict1 = dict1.copy()  
merged_dict1.update(dict2)  
merged_dict1.update(dict3)  
print("Merged Dictionary using update():", merged_dict1)

