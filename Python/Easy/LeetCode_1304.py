# Given an integer n, return any array containing n unique integers such that they add up to 0.


class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid = n // 2
        ans = []

        for i in range(1, mid+1):
            ans.append(i)
            ans.append(-i)

        if n%2 != 0:
            ans.append(0)

        return ans