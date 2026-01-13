nums = [1,5,7,-1,5]
n = len(nums)
target_sum = 6
pairs = []
pairs_count = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target_sum:
            pairs.append((nums[i], nums[j]))
            pairs_count += 1

print(pairs)
print(pairs_count)