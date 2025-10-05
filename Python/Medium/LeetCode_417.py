# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        ln, wd = len(heights), len(heights[0])

        for j in range(wd):
            p_que.append((0,j))
            p_seen.add((0,j))

        for i in range(1, ln):
            a_que.append((i,0))
            a_seen.add((i,0))

        for i in range(ln):
            a_que.append((i, wd-1))
            a_seen.add((i, wd-1))

        for j in range(wd-1):
            a_que.append((ln-1, j))
            a_seen.add((ln-1, j))

        def getCords(que, seen):
            cords = set()

            while que:
                i, j = que.popleft()

                for i_off, j_off in [(0,1), (1,0), (0, -1), (-1, 0)]:
                    r, c = i + i_off, j + j_off

                    if 0 <= r < ln and 0 <= c < wd and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))


        getCords(p_que, p_seen)
        getCords(a_que, a_seen)

        return list(p_seen.intersection(a_seen))