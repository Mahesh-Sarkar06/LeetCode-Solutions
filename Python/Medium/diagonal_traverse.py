# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Get size of rows & cols
        rows, cols = len(mat), len(mat[0])
        # Defined a hash map for keep track of elements at certain position
        mp = {}
        # Defined empty list for storing the correct order of diagonal values
        res = []
        # Boolean value to toggle the direction of diagonal values
        isFlip = True

        # Iterate through rows & cols
        for r in range(rows):
            for c in range(cols):
                # If sum of row & col position exist in hash map -> append the value from mat
                if (r+c) in mp:
                    mp[r+c].append(mat[r][c])
                # If not -> create new key value in hash map
                else:
                    mp[r+c] = [mat[r][c]]

        # Iterate through hash map
        for key, val in mp.items():
            # If isFlip is True -> values for that key should get reversed
            if isFlip:
                val.reverse()

            # Iterate through each elements in the value & append in the final list
            for v in val:
                res.append(v)

            # Toggle the isFlip value -> alterate toggling for each diagonal traverse
            isFlip = not isFlip

        return res