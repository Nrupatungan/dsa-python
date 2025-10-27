# Count negative numbers in a sorted array min

# Given a m x n matrix grid which is sorted in non-increasing order both
# row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0


def countNegatives(grid: list[list[int]]) -> int:
    count_neg = 0
    for m in range(len(grid)):
        for n in range(len(grid[m])):
            if grid[m][n] < 0:
                count_neg += 1

    return count_neg


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
grid2 = [[3, 2], [1, 0]]

print(countNegatives(grid))
print(countNegatives(grid2))
