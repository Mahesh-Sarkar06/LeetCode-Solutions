# You are given a 2D 0-indexed integer array dimensions.

# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.


class Solution:
    def areaOfMaxDiagonal(self, dimension: List[List[int]]) -> int:
        # Initialized maximum diagonal and area
        maxDiag = 0
        maxArea = 0

        # Iterating through each dimension pair
        for dim in dimension:
            # Fetched length and width of the rectangle
            l = dim[0]
            w = dim[1]
            # Calculated diagonal and area value for current dimension pair
            currDiag = (l*l) + (w*w)
            currArea = l*w

            # Check if calculated diagonal is greater than initialized diagonal
            if currDiag > maxDiag:
                # Setting the maximum diagonal value and area corresponding to this pair
                maxDiag = currDiag
                maxArea = currArea
            # If calculated and max diagonal are of same length
            elif currDiag == maxDiag:
                # Compare the area and set it to max area
                maxArea = max(maxArea, currArea)

        return maxArea