
#bubble sort implementation


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
array = [64, 34, 25, 12, 22, 11, 90,15,9]
sorted_array = bubble_sort(array)
print(" bubble Sorted array:", sorted_array)
