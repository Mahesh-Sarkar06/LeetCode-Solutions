# You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

# Return the minimum possible area of the rectangle.


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Size of rows and cols in the matrix
        rows, cols = len(grid), len(grid[0])
        # Initialized min and max values of rows and cols
        minRow = rows
        maxRow = -1
        minCol = cols
        maxCol = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Updating min and max values of rows and cols value
                    minRow = min(minRow, row)
                    maxRow = max(maxRow, row)
                    minCol = min(minCol, col)
                    maxCol = max(maxCol, col)
                    
        # Returning the min area required to cover all ones
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)