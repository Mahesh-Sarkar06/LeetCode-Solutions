# You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

# Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

# You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

# Return the minimum possible score that you can achieve with some triangulation of the polygon.


from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        self.values = values

        return self.dynamicTriangles(0, len(values)-1)
    

    def dynamicTriangles(self, v1: int, v3: int) -> int:
        if v3 - v1 < 2:
            return 0
        
        res = float('inf')
        for v2 in range(v1+1, v3):
            curr = self.values[v1] * self.values[v2] * self.values[v3]
            res = min(res, curr + self.dynamicTriangles(v1, v2) + self.dynamicTriangles(v2, v3))

        return res