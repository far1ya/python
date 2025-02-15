def check_consecutive(lst):
    lst.sort()
    
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1] + 1:
            return False
    
    return True

input_list = [4, 2, 3, 1, 5]
if check_consecutive(input_list):
    print("The list contains consecutive integers.")
else:
    print("The list does not contain consecutive integers.")
