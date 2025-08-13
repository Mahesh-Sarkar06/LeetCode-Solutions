# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Note: -2**31 <= n <= 2**31 - 1 (32 bit values)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 3^20 will be the first integer value that will exceed 32-bit integer value
        return n > 0 and 3**20%n == 0