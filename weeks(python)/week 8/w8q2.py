
list1_input = input("Enter the first list of elements, separated by spaces: ")
list1 = list1_input.split() 

list2_input = input("Enter the second list of elements, separated by spaces: ")
list2 = list2_input.split() 

union_list = list(set(list1) | set(list2))

print("Union of the two lists:", union_list)
