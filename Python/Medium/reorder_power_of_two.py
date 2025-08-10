# You are given an integer n. We reorder the digits in any order (including the original order)
# such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.


'''
So, as per the question we have to check if any reordered value of given integer can be expressed as a power of 2.
For this, we can either check for each combination & apply AND operation on it with 1 less than that number,
and check if that result in 0. But this will be a very complex and long running query since the constraint is
0 <= n <= 10^9.

Now, another approach we can have that if we first memoize the sorted value of power of 2 and check that with
sorted value of input integer.
'''

class Solution:
    def __init__(self):
        # Generating all power of 2 values till power 31 using Left Shift operator
        # For every value of i, binary 1 is left shifted
        # 1(000001) << i = 4 -> 01000 (8): 2^3
        self.possibility = {''.join(sorted(str(1 << i))) for i in range(31)}

    def reorderedPowerOf2(self, n: int) -> bool:
        # Checking of sorted order of n exist in possibility (memoization)
        return ''.join(sorted(str(n))) in self.possibility