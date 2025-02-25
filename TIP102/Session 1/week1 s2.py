
# def nana_batmatrixan(x):
#     pass
#
#
#
# nana_batmatrixan(0)
# nana_batmatrixan(-2)
# nana_batmatrixan(2)


matrix = [[1, 2], [3, 4], [5, 6]]
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Initialize an empty matrix for the transpose
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed
