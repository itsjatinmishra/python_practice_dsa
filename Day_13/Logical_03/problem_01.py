def combinations_of_two(nums):
    result = []
    size = len(nums)

    for i in range(size):
        for j in range(i + 1, size):
            result.append([nums[i], nums[j]])

    return result


nums = [1, 2, 3]
print(combinations_of_two(nums))
