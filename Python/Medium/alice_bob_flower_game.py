# Alice and Bob are playing a turn-based game on a field,
# with two lanes of flowers between them.
# There are x flowers in the first lane between Alice and Bob,
# and y flowers in the second lane between them.

# The game proceeds as follows:

# Alice takes the first turn.
# In each turn, a player must choose either one of the lane and pick one flower from that side.
# At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.
# Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

# Alice must win the game according to the described rules.
# The number of flowers x in the first lane must be in the range [1,n].
# The number of flowers y in the second lane must be in the range [1,m].
# Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.



class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Seggregating odd and even counts
        n_odd = n // 2
        n_even = n // 2
        # Check for odd or even value of n
        if n%2 != 0:
            n_odd += 1

        # Seggregating odd and even counts
        m_odd = m // 2
        m_even = m // 2
        # Check for odd and even values of m
        if m%2 != 0:
            m_odd += 1

        return (n_odd * m_even) + (n_even * m_odd)