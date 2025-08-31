# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Fill initial sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3)*3 + (c//3)].add(num)

        def backtrack():
            if not empty:
                return True  # solved!

            # pick the cell with the least candidates (MRV heuristic)
            r, c = min(empty, key=lambda x:
                       9 - len(rows[x[0]] | cols[x[1]] | boxes[(x[0]//3)*3 + (x[1]//3)]))

            empty.remove((r, c))
            b = (r//3)*3 + (c//3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    if backtrack():
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            empty.append((r, c))
            return False

        backtrack()