def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

array = [5, 3, 7, 2, 8]
target = 8
result = linear_search(array, target)

if result != -1:
    print("linear search Element found at index:", result)
else:
    print("Element not found.", result)
