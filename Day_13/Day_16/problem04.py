# Write a program to sort an array using Merge Sort and print the sorted array.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    #merge while comparing
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [40,30,20,10, 88, 10, 65, 98]
print(merge_sort(arr))