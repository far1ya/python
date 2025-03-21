def sort_list(elements):
    elements.sort() 
    return elements
user_input = input("Enter a list of elements separated by spaces: ")

elements = list(map(int, user_input.split()))

sorted_elements = sort_list(elements)

print("Sorted List:", sorted_elements)
