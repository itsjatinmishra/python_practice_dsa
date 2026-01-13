import ast

# Read input
data = ast.literal_eval(input())
matrix = data[0]
k = data[1]

n = len(matrix)

# Rotate k times (each rotation = 90 degrees clockwise)
for rotation in range(k % 4):
    # Create empty rotated matrix
    rotated = [[0] * n for _ in range(n)]
    
    # Fill rotated matrix using simple formula
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    
    matrix = rotated

print(matrix)