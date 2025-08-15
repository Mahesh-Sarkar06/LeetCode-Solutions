# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        powerOfFour = 1
        while powerOfFour < n:
            powerOfFour *= 4

        return powerOfFour == n
    


# Above takes Time Complexity O(log n) and Space Complexity O(1).
# Let's take Time Complexity to O(1) by removing loops

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Here checking 3 conditions:
        # Given number should be greater than 0
        # Given number can be represented by Power of 2
        # And last final: Check bitwise AND operation with hexadecimal value of 5
        # 0x5 = 0101
        # 0x55 = 0101 0101
        # 0x555 = 0101 0101 0101
        # All 1's are available at even position
        return n > 0 and (n & (n-1)) == 0 and (n & 0x55555555) != 0