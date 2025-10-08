# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


from typing import List

class Solution:
    def successfulPair(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        size = len(potions)
        res = []

        def binarySearch(ele: int) -> int:
            left = 0
            right = size - 1

            while left <= right:
                mid = left + (right - left) // 2

                if potions[mid] * ele >= success:
                    right = mid - 1
                else:
                    left = mid + 1
                
                return left
            
            for s in spells:
                res.append(size - binarySearch(s))

            return res