
list1_input = input("Enter the first list of elements, separated by spaces: ")
list1 = list(map(int, list1_input.split()))  

list2_input = input("Enter the second list of elements, separated by spaces: ")
list2 = list(map(int, list2_input.split()))  

intersection_list = list(set(list1) & set(list2))

print("Intersection of the two lists:", intersection_list)
