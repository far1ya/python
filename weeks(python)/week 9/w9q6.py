arr = list(map(int, input("Enter numbers separated by space: ").split()))
search_element = int(input("Enter the element you want to search for: "))

if search_element in arr:
    print(f"The element {search_element} is found in the list.")
else:
    print(f"The element {search_element} is not found in the list.")
