arr = [5, 1, 4, 2, 8]
size = len(arr)

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    iteration = 0
    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                iteration += 1
                swap(arr, j, j + 1)
    return iteration

print("No of passes are: ", bubble_sort(arr))
print("Sorted list is : ", arr)
