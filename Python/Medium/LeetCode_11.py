# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lft = 0
        rgt = len(height) - 1
        max_Area = 0

        while lft < rgt:
            ht = min(height[lft], height[rgt])
            wd = rgt - lft
            area = ht * wd

            max_Area = max(max_Area, area)

            if height[lft] > height[rgt]:
                rgt -= 1
            else:
                lft += 1

        return max_Area