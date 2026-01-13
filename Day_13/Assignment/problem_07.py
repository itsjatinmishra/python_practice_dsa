def is_magic_square(matrix):

    # Check if matrix is square
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return "The given matrix is not a magic matrix"

    row_s = len(matrix)
    col_s = len(matrix[0])

    rows_sum = []
    cols_sum = []
    digonal = []

    # diagonal calculation
    first_digonal = 0
    second_digonal = 0
    col_temp = col_s - 1

    for i in range(row_s):
        first_digonal += matrix[i][i]
        second_digonal += matrix[i][col_temp]
        col_temp -= 1

    digonal.append(first_digonal)
    digonal.append(second_digonal)

    # row & column calculation
    for i in range(row_s):
        row_sum = 0
        col_sum = 0

        for j in range(col_s):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

        rows_sum.append(row_sum)
        cols_sum.append(col_sum)

    # Merge all sums
    final_list = rows_sum + cols_sum + digonal

    # Check if all sums are same
    initial_element = final_list[0]

    for item in final_list:
        if item != initial_element:
            return "The given matrix is not a magic matrix"

    return "The given matrix is a magic matrix"


# ---- Example ----
matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

print(is_magic_square(matrix))