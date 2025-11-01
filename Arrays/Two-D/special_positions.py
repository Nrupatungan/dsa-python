# Special positions in a binary matrix

# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements
# in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:
# | 1 0 0 |
# | 0 0 1 |
# | 1 0 0 |

# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]

# Output: 1

# Explanation: (1, 2) is a special position
# because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.


# Example 2:
# | 1 0 0 |
# | 0 1 0 |
# | 0 0 1 |

# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.


def num_Special(mat: list[list[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    row_count = [0] * m
    col_count = [0] * n

    for row in range(m):
        for col in range(n):
            if mat[row][col] == 1:
                row_count[row] += 1
                col_count[col] += 1

    ans = 0
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1 and row_count[r] == 1 and col_count[c] == 1:
                ans += 1

    return ans


mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

print(num_Special(mat))
print(num_Special(mat2))
