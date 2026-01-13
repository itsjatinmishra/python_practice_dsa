# Combine Binary Search with Insertion Sort to insert an element into a sorted array.

arr = [10, 20, 30, 50, 60]

element_to_insert = 40

def binary_search(arr, element_to_insert):
    size = len(arr)
    s = 0
    e = size - 1
    index = -1
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] < element_to_insert:
            s = mid + 1
        
        elif arr[mid] > element_to_insert:
            e = mid - 1
        else:
            return mid
            
    return s

insert_index = binary_search(arr, element_to_insert)
# increase list size by one position
arr.append(None)

i = len(arr) - 1
while i > insert_index:
    arr[i] = arr[i-1]
    i -= 1

arr[insert_index] = element_to_insert

print(arr)