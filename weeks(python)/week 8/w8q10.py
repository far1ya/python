def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

   
    while low <= high:
        mid = (low + high) // 2  

       
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input("Enter the target number to search for: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
