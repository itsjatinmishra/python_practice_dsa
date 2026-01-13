arr = [8,4,2,48,14,98,100,92,99]
def merge_sort(arr):
    if len(arr) <= 1:        # base case
        return arr

    mid = len(arr) // 2      # find middle
    left = merge_sort(arr[:mid])     # sort left half
    right = merge_sort(arr[mid:])    # sort right half

    return merge(left, right)        # merge both halves

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]

    return result

