# Transpose matrix

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped
# over its main diagonal, switching the matrix's row and column indices.

# |   2   4   -1   |        |  2  -10   18  |
# | -10   5   11   |  ==>   |  4    5   -7  |
# |  18  -7    6   |        | -1   11    6  |


# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]


# Example 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]


def transpose(mat: list[list[int]]) -> list[list[int]]:
    m = len(mat)
    n = len(mat[0])

    trans_mat = [[0 for _ in range(m)] for _ in range(n)]

    for c in range(n):
        for r in range(m):
            trans_mat[c][r] = mat[r][c]

    return trans_mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[1, 2, 3], [4, 5, 6]]

print(transpose(mat))
print(transpose(mat2))
