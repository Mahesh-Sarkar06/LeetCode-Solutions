# Given an m x n binary matrix mat, return the number of submatrices that have all ones.

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Check if matrix is NULL or not
        if not mat or not mat[0]:
            return 0
        
        rows, cols = len(mat), len(mat[0])
        height = [0] * cols
        total = 0

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    height[col] += 1
                else:
                    height[col] = 0

            stack = []
            count = [0] * cols
            for col in range(cols):
                while stack and height[stack[-1]] > height[col]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    count[col] = count[prev]
                    count[col] += height[col] * (col - prev)
                else:
                    count[col] = height[col] * (col + 1)

                stack.append(col)
                total += count[col]

        return total