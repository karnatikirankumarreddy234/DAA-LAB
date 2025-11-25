def counting_sort(arr):
    if not arr:
        return arr
    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            arr[index] = num
            index += 1
    return arr

# Example usage:
array = [4, 2, 2, 8, 3, 3, 1,000,823,1]
sorted_array = counting_sort(array)
print(" counting Sorted array:", sorted_array)
