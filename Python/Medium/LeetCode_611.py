# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


from typing import List

class Solution:
    def triangle(self, nums: List[int]) -> int:
        # Sorting the values of in increasing order
        nums.sort()
        # Total length of array list
        size = len(nums)
        # Defined variable to store the triangle pair
        res = 0

        # Initialize the pointer at last position
        for k in range(size - 1, 1, -1):
            # Initialize another pointer at second last position
            j = k - 1
            # Initialize a pointer at first position
            i = 0

            # Loop until first position pointer reaches the second last position
            while i < j:
                # Check if the sum of the ith & jth element is greater than kth element
                if nums[i] + nums[j] > nums[k]:
                    # If True -> add to res
                    res += j - i
                    # Position down the j pointer
                    j -= 1
                else:
                    # If False -> move up the ith position
                    i += 1

        return res