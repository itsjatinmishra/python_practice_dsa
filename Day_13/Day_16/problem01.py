# Write a program to sort an array using Bubble Sort
# and count the number of swaps.

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    swap_count = 0
    size = len(arr)
    for i in range(size):
        for j in range(size - 1 - i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j + 1)
                swap_count += 1
    return arr, swap_count

arr = [98,56,34,2,100,88]

output_list, count = bubble_sort(arr)

print("The sorted list is : ", output_list)
print("The number of swaps are: ", count)


