# Given a positive integer n, there exists a 0-indexed array called powers, 
# composed of the minimum number of powers of 2 that sum to n.
# The array is sorted in non-decreasing order, and there is only one way to form the array.

# You are also given a 0-indexed 2D integer array queries,
# where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find
# the product of all powers[j] with lefti <= j <= righti.

# Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query.
# Since the answer to the ith query may be too large, each answers[i] should be returned modulo 10^9 + 7.


MOD = 10**9 + 7

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Extract powers of 2 from n
        powers = [1 << i for i in range(32) if (n & (1 << i))]
        
        # Step 2: Build prefix product array
        prefix_prod = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix_prod[i+1] = (prefix_prod[i] * powers[i]) % MOD
        
        # Step 3: Answer each query using O(1) formula
        ans = []
        for l, r in queries:
            prod = (prefix_prod[r+1] * pow(prefix_prod[l], MOD-2, MOD)) % MOD
            ans.append(prod)
        
        return ans