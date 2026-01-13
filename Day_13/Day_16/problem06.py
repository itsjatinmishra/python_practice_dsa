#6.	Implement Binary Search on a sorted array and return the index of the target.

list_01 = [5,8,26,66,98]


target = 26
def binary_search(list_01, target):
    start = 0
    end = len(list_01) - 1
    while start <= end:
        mid = (start + end) // 2

        if list_01[mid] == target:
            return mid
        elif list_01[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search(list_01, target))