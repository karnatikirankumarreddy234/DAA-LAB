def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1  # Target not found

sorted_array = [2, 3, 5, 7, 8,0,186,4]
target =3
result = binary_search(sorted_array, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.", result)
