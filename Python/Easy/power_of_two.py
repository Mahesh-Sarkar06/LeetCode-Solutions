# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2^x.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
    

#------------------------------- Explanation -------------------------------#
'''
In binary system, we know powers of 2 are represented as sequence of one 1's and rest 0's
For eg: 2 -> 10, 4 -> 100, 8 -> 1000 ...
So, we are just checking for if passed value is powers of 2 or not. And subtracting 1 from it will result
in all 0's in 1 and 1 to 0
For eg: 8 -> 1000, 7 -> 0111
Then applying AND operation should always result in 0 [1000 & 0111] = 0000
'''