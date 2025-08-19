# Given an integer array nums, return the number of subarrays filled with 0.

# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # Maintain count of consecutive zero's
        count = 0
        # Check for zero's sub array count
        ans = 0

        for num in nums:
            if num == 0:
                count += 1
                ans += count
            else:
                count = 0

        return ans