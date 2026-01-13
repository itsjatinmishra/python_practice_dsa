#Use Insertion Sort to insert elements into a sorted array one by one.
arr = [40,30,20,10]

def insertion_sort(arr):
    size = len(arr)
    for i in range(size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(arr))