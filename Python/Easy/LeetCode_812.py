# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three different points.

# Answers within 10^-5 of the actual answer will be accepted.


from typing import List

class Solution:
    # Defined a function for calculating area using 3 different points
    def area(self, p1: List[int], p2: List[int], p3: List[int]) -> float:
        # X, Y coordinates of each points
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        # Return the area using Gauss's Area formula (Shoelace formula)
        return abs(
            x1 * (y2 - y3) +
            x2 * (y3 - y1) +
            x3 * (y1 - y2)
        ) * 0.50000
    

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Initialize a variable to store maximum area
        max_area = 0.00000

        # Iterating through every coordinates in points and position index to 3 consecutive coordinates
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    # Calculate area using above function
                    ar = self.area(points[i], points[j], points[k])

                    max_area = max(max_area, ar)

        return max_area