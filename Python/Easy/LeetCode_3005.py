# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.


from collections import defaultdict
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fm = defaultdict(int)
        res = 0

        for num in nums:
            fm[num] += 1

        vals = fm.values()
        max_val = max(vals)

        for val in vals:
            if val == max_val:
                res += val

        return val