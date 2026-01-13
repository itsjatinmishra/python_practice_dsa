# Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:   # base case
        return arr

    pivot = arr[0]
    smaller = []
    bigger = []

    for x in arr[1:]:
        if x < pivot:
            smaller.append(x)
        else:
            bigger.append(x)

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)


list_01 = [3, 6, 8, 10, 1, 2, 1]

print(quick_sort(list_01))