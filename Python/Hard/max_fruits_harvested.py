# Fruits are available at some positions on an infinite x-axis.
# You are given a 2D integer array fruits where fruits[i] = [positioni, amounti]
# depicts amounti fruits at the position positioni. fruits is already sorted by positioni
# in ascending order, and each positioni is unique.

# You are also given an integer startPos and an integer k. Initially, you are at the position startPos.
# From any position, you can either walk to the left or right. It takes one step to move one unit
# on the x-axis, and you can walk at most k steps in total.
# For every position you reach, you harvest all the fruits at that position,
# and the fruits will disappear from that position.

# Return the maximum total number of fruits you can harvest.


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        size = len(fruits)
        total = 0
        res = 0

        def steps(l, r):
            if fruits[l][0] >= startPos:
                return fruits[r][0] - startPos
            elif fruits[r][0] <= startPos:
                return startPos - fruits[l][0]
            else:
                return min(startPos - fruits[l][0], fruits[r][0] - startPos) + fruits[r][0] - fruits[l][0]

        l = 0
        for r in range(size):
            total += fruits[r][1]

            while l <= r and steps(l, r) > k:
                total -= fruits[l][1]
                l += 1

            res = max(res, total)

        return res