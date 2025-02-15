
list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]

merged_list = list1 + list2

merged_list.sort()

print("Merged and sorted list:", merged_list)
