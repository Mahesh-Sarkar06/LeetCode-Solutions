# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Size of rows and columns
        r, c = len(matrix), len(matrix[0])
        # Count for each sub array
        total = 0
        # Zero matrix to track for every possible values
        dp = [[0] * n for _ in range(m)]

        # Iterate through each element of the matrix
        for i in range(r):
            for j in range(c):
                # Check if element is 1 or not
                if matrix[i][j] == 1:
                    # Check if either index is starting index or not
                    if i == 0 or j == 0:
                        # replace with 1 at that position in dp matrix
                        dp[i][j] = 1
                    else:
                        # If not then put 1 incremented value from the min upper half dp matrix
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

                    # Add the current index value to count the sub matrix of 1
                    total += dp[i][j]

        return total