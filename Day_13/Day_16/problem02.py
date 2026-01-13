# Implement Selection Sort to arrange a list of integers in descending order.
arr = [26,66,98, 5, 8]

def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        max_index = i
        for j in range(i + 1, size):
            if arr[j] > arr[max_index]:
                max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort(arr))