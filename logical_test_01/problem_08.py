matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

row_size = len(matrix)
col_size = len(matrix[0])

# Initialize output_matrix with same dimensions
output_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]

for i in range(row_size):
    for j in range(col_size):
        output_matrix[i][j] = matrix[j][i]

print(output_matrix)
if output_matrix == matrix:
    print(True)
else:
    print(False)