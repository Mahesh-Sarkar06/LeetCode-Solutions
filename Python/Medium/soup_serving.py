# You have two soups, A and B, each starting with n mL. On every turn,
# one of the following four serving operations is chosen at random,
# each with probability 0.25 independent of all previous turns:
#   pour 100 mL from type A and 0 mL from type B
#   pour 75 mL from type A and 25 mL from type B
#   pour 50 mL from type A and 50 mL from type B
#   pour 25 mL from type A and 75 mL from type B

# Note:
#   There is no operation that pours 0 mL from A and 100 mL from B.
#   The amounts from A and B are poured simultaneously during the turn.
#   If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.
#   The process stops immediately after any turn in which one of the soups is used up.

# Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn.
# Answers within 10-5 of the actual answer will be accepted.


#-------------------------------- EXPLANATION --------------------------------#
'''
As per the questions we have 4 operations which can be performed. And using that we have 3 conditions:
    1. If A is emptied first -> Probability is 1
    2. If B is emptied first -> Probability is 0
    3. If A & B both emptied together -> Half of the Probability of A

Also, we have the constraint 0 <= n <= 10^9
So, for higher values, say 15000, probability of emptying A tends to 1 since A can be used completely,
whereas B is never be used completely. Thus probability of emptying B will tends to 0.
'''

import math

class Solution:
    def __init__(self):

        # Scaled down volumes as per 25mL, eg: 100mL -> 4, 75mL -> 3, 50mL -> 2, 25mL -> 1
        self.ops = [(4,0), (3,1), (2,2), (1,3)]

        # Emptied dictionary for memoization
        self.memo = {}


    def solve(self, A: int, B: int) -> float:
        # First we check for both are emptied for not
        if (A <= 0 and B <= 0):
            return 0.5
        
        # A is emptied first
        if A <= 0:
            return 1.0
        
        # B is emptied first
        if B <= 0:
            return 0.0
        
        # Checking for (A,B) value already computed and its probability exists -> Memoization
        if (A,B) in self.memo:
            return self.memo[(A,B)]
        
        prob = 0.0
        # Iterating and taking the bowl values as per the operations
        for k, v in self.ops:
            takenA = A - k
            takenB = B - v

            prob += self.solve(takenA, takenB)

        prob *= 0.25
        self.memo[(A,B)] = prob

        return prob
    

    def soupServings(self, n: int) -> float:
        # Checking at starting we have both emptied soup bowls -> Prob: 0.5
        if n == 0:
            return 0.5
        
        n = math.ceil(n/25)

        # Now, check if bowl value is greater than threshold -> Prob ~ 1
        if n > 480:
            return 1.0
        
        return self.solve(n, n)