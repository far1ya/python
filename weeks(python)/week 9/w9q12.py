def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # If there are remaining elements in left or right, add them
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Merge Sort function
def merge_sort(arr):
    # Base case: if the array is a single element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_half, right_half)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)

sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
