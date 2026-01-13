matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_size = len(matrix)
col_size = len(matrix[0])

# Initialize output_matrix with same dimensions
output_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]

for i in range(row_size):
    for j in range(col_size):
        output_matrix[col_size - 1 - j][i] = matrix[i][j]

print(output_matrix)