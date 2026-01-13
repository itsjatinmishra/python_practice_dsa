def longest_consecutive(nums):
    nums_set = set(nums)   # Convert list to set for fast search
    longest = 0

    for n in nums_set:
        # Check if this is the START of a sequence
        if n - 1 not in nums_set:
            print(n-1)
            length = 1
            next_num = n + 1

            # Keep checking next consecutive numbers
            while next_num in nums_set:
                length += 1
                next_num += 1

            # Update longest sequence length
            longest = max(longest, length)

    return longest


# Test
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4