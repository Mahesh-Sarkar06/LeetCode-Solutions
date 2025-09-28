# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1, 1, -1):
            curr = nums[i-2] + nums[i-1]

            if curr > nums[i]:
                return curr + nums[i]
            
        return 0