# When a child enters a room, they will collect all the fruits there.
# If two or more children enter the same room, only one child will collect the fruits,
# and the room will be emptied after they leave.

# Return the maximum number of fruits the children can collect from the dungeon.


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        size = len(fruits)  # Total elements in List
        res = sum(fruits[i][i] for i in range(size))    # Sum of diagonal elements of the List

        # Function to for other 2 diagonal position element calculation
        def matrix():
            # Empty Array of same size
            grid = [[0] * size for _ in range(size)]

            # Calculation for top right element
            grid[0][size-1] = fruits[0][size-1]

            # Iterating through the elements
            for i in range(1, size-1):
                # Comparing sum of elements at (1,2), (1,3) for maximum collection
                for j in range(max(i+1, size-1-i), size):
                    top = grid[i-1][j]
                    top = max(top, grid[i-1][j-1])

                    if j < size-1:
                        top = max(top, grid[i-1][j+1])

                    grid[i][j] = top + fruits[i][j]
            return grid[size-2][size-1]

        # Adding the collected values from above to diagonal sum result
        res += matrix()

        # Transposing the matrix
        for i in range(size):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        # Calling the same algorithm to calculate max value
        res += matrix()

        return res