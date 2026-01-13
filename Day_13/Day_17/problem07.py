
def rotate_a_list_with_k_value(arr, k):
    size = len(arr)

    # no rotation needed
    if k == 0 or k % size == 0:
        return arr
    
    k = k % size

    back = arr[size - k: ]

    front = arr[:size - k]

    print(back, front)

    final_output = back + front
    return final_output


arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_a_list_with_k_value(arr, k))