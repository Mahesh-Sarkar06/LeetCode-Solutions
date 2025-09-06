# You are given a 2D array queries, where queries[i] is of the form [l, r].
# Each queries[i] defines an array of integers nums consisting of elements ranging from l to r, both inclusive.

# In one operation, you can:

# Select two integers a and b from the array.
# Replace them with floor(a / 4) and floor(b / 4).
# Your task is to determine the minimum number of operations required to reduce all elements of the array to zero for each query.
# Return the sum of the results for all queries.


class Solution:
    def _getOperations(self, val: int) -> int:
        res = 0
        ops = 0
        pof = 1

        while pof <= val:
            lft = pof
            rgt = min(val, pof * 4 - 1)
            ops += 1
            res += (rgt - lft + 1) * ops
            pof *= 4

        return res


    def minOperations(self, queries: List[List[int]]) -> int:
        return (
            sum((self._getOperations(rgt) - self._getOperations(lft-1) + 1) // 2)
            for lft, rgt in queries
        )