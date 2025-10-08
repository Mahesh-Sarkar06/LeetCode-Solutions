# Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

# Given an integer array rains where:

# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:

# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

# Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        lastRainDay = {}         # lake -> last day it rained there
        sunnyDays = []            # sorted list of indices of sunny days

        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in lastRainDay:
                    # need to dry it before day i
                    prev = lastRainDay[lake]
                    # find a sunny day > prev
                    j = bisect.bisect_right(sunnyDays, prev)
                    if j == len(sunnyDays):
                        return []
                    day_to_dry = sunnyDays.pop(j)
                    ans[day_to_dry] = lake
                lastRainDay[lake] = i
                ans[i] = -1
            else:
                # sunny day
                sunnyDays.append(i)
                ans[i] = 1  # default, but may be overridden later

        return ans