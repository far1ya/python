
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1  # Index of the previous element

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at the correct position
        arr[j + 1] = key
        
        # Visualize the intermediate list after each step
        print(f"Step {i}: {arr}")

# Taking input from the user
arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Calling the insertion_sort function to sort the list and visualize intermediate steps
print("\nInitial array:", arr)
insertion_sort(arr)
print("\nSorted array:", arr)
