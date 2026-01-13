# Write a Python function that takes a matrix (2D list) 
# and returns the transpose of the matrix without using 
# any built-in methods. Example: 
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
  


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(transpose(matrix))
