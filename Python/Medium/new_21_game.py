# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets k or more points.

# Return the probability that Alice has n or fewer points.

# Answers within 10-5 of the actual answer are considered accepted.


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        
        dp = [0.0] * (n + maxPts + 1)
        
        for i in range(k, n+1):
            dp[i] = 1.0

        windowSum = min(n-k+1, maxPts)
        for j in range(k-1, -1, -1):
            dp[j] = windowSum/maxPts

            windowSum += dp[j] - dp[j+maxPts]

        return dp[0]