# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).


import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Size of the grid
        n = len(grid)
        # Defined a heap with (time, row, col)
        heap = [(grid[0][0], 0, 0)]
        # Defined a set of (row, col) which have been visited
        seen = set([(0,0)])
        
        # Until heap is not empty
        while heap:
            # Fetch (time, row, col) from heap
            time, r, c = heapq.heappop(heap)

            # Check if (row, col) has reached to last cell of the grid -> return the time
            if r == n-1 and c == n-1:
                return time
            
            # For every row, col in the defined list
            for dr, dc in [(0,1), (1,0), (0, -1), (-1, 0)]:
                # New row, col values
                nr, nc = r + dr, c + dc

                # Check if new row & col is less than the size of grid and has not been visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    # Add to visited set and push to the heap
                    seen.add((nr, nc))
                    heapq.heappush(heap, (max(grid[nr][nc], time), nr, nc))