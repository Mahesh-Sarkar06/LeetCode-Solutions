# A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

# Implement the Spreadsheet class:

# Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
# void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
# void resetCell(String cell) Resets the specified cell to 0.
# int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
# Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.


class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = [[0] * 26 for i in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        self.grid[int(cell[1:])][ord(cell[0]) - ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.grid[int(cell[1:])][ord(cell[0]) - ord('A')] = 0

    def getValue(self, formula: str) -> int:
        curr = formula[1:].split('+')
        res = 0

        for val in curr:
            if val.isdigit():
                res += int(val)
            else:
                res += self.grid[int(val[1:])][ord(val[0]) - ord('A')]

        return res