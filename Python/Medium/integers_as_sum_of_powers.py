# Given two positive integers n and x.

# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers,
# in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1^x + n2^x + ... + nk^x.

# Since the result can be very large, return it modulo 10^9 + 7.

# For example, if n = 160 and x = 3, one way to express n is n = 2^3 + 3^3 + 5^3.


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [1] + [0] * n  # dp[i] = number of ways to make sum i
        
        base = 1
        while True:
            power = base**x
            if power > n:
                break
            for i in range(n, power - 1, -1):
                dp[i] = (dp[i] + dp[i - power]) % MOD
            base += 1
        
        return dp[n]