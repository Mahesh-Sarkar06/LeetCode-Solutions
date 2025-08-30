# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for each row
        for row in range(9):
            # Defined an empty hash set for storing unique values
            hashSet = set()
            for col in range(9):
                ele = board[row][col]
                # Check if element exist in hash set
                if ele in hashSet:
                    return False
                # if not exist -> add to hash set
                elif ele != '.':
                    hashSet.add(ele)

        # Check for each col
        for row in range(9):
            hashSet = set()
            for col in range(9):
                ele = board[col][row]
                if ele in hashSet:
                    return False
                elif ele != '.':
                    hashSet.add(ele)

        # starting position of each 3x3 matrix box
        pos = [(0, 0), (0, 3), (0, 6),
               (3, 0), (3, 3), (3, 6),
               (6, 0), (6, 3), (6, 6)]
        
        # Validate each 3x3 matrix
        for r, c in pos:
            hashSet = set()
            for row in range(r, r+3):
                for col in range(c, c+3):
                    ele = board[row][col]
                    if ele in hashSet:
                        return False
                    elif ele != '.':
                        hashSet.add(ele)


        return True