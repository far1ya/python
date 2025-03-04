
def sort_by_length(lst):
    return sorted(lst, key=len)

user_input = input("Enter a list of words, separated by spaces: ")

my_list = user_input.split()

sorted_list = sort_by_length(my_list)

print("Sorted list by length:", sorted_list)
