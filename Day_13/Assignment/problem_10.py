list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8] 

def merge_sort(list1, list2):
    i = 0
    j = 0

    l1 = len(list1)
    l2 = len(list2)

    output = []
    while i < l1 and j < l2:
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1
            
    # Add remaining elements from either list
    while i < l1:
        output.append(list1[i])
        i += 1
    while j < l2:
        output.append(list2[j])
        j += 1

    return output


print(merge_sort(list1, list2))