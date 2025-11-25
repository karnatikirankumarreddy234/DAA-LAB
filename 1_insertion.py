
#  1) insertion sort implemention

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
my_list = [12, 11, 13, 5, 6,15,9]
sorted_list = insertion_sort(my_list)
print("Sorted array:", sorted_list)



