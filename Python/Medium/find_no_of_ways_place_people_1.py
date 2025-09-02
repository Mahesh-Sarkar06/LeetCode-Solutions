# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

# Count the number of pairs of points (A, B), where

# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Total number of coordinates
        size = len(points)
        # Variable to store count
        count = 0

        # Iterate through the coordinates pair
        for i in range(size):
            # Get x-coordinate and y-coordinate
            ax, ay = points[i]
            for j in range(size):
                # Check if same coordinate is referred
                if i == j:
                    continue

                # Get next x and y coordinate
                bx, by = points[j]
                # Check if prev coordinate is not at top left
                if not (ax <= bx and ay >= by):
                    continue

                # Flag to check position of third coordinate
                skip = False
                for k in range(size):
                    # Check if current coordinate is same as prev two coordinate
                    if k == i or k == j:
                        continue

                    # Get next x and y coordinate
                    cx, cy = points[k]
                    # Check if third coordinate is in between the prev two coordinate
                    if (cx >= ax and cx <= bx) and (cy <= ay and cy >= by):
                        skip = True
                        continue

                # If above condition is TRUE -> increase the count
                if skip:
                    count += 1
                    
        return count