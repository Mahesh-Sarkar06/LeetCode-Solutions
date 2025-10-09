# You are given two integer arrays, skill and mana, of length n and m, respectively.

# In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

# Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

# Return the minimum amount of time required for the potions to be brewed properly.


from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m, n = len(mana), len(skill)
        pre_skill = [0] * n

        for i in range(m):
            curr_time = 0
            for j in range(n):
                curr_time = max(curr_time, pre_skill[j]) + skill[j] * mana[i]

            pre_skill[n-1] = curr_time
            for j in range(n-2, -1, -1):
                pre_skill[j] = pre_skill[j+1] - skill[j-1] * mana[i]

        return pre_skill[n-1]