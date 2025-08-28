# You are given an n x n square matrix of integers grid. Return the matrix such that:

# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Get size of matrix
        rows, cols = len(grid), len(grid[0])
        # Empty dict for storing specific diagonal elements
        diag = {}

        # Iterating through matrix
        for r in range(rows):
            for c in range(cols):
                # Check for specific diagonal value
                # For upper diagonal elements -> they lie in 0,1 and 1,2. Difference (1-0), (2-1) is 1
                # If this value exist in diag dict, then append that element
                if (c - r) in diag:
                    diag[c - r].append(grid[r][c])
                # If not then create new key val pair
                else:
                    diag[c - r] = [grid[r][c]]

        # For upper diagonals, sort them in ascending order
        # For lower & longest diagonal, sort them in descending order
        for key, val in diag.items():
            if key > 0:
                val.sort()
            else:
                val.sort(reverse=True)

        # Once sorted, replace the original grid elements with sorted values
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                grid[r][c] = diag[c - r].pop()

        return grid