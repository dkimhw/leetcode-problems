
"""

Input: 9 x 9 array rep of sudoku board
Output: boolean
  - True if valid, False if not
  - Only the filled cells need to be validated according to the mentioned rules.
  - Unique digits in row, col, and 3 x 3 box


Algorithm:
- Loop through each row: check that the digits are distinct
  - Return false if they are distinct
  - Generate column for each row we loop through
    - current index for all nine rows [ curr[idx] for row in board ]
    - Return false if they are distinct
- Find the appropriate 3 x 3 box:
  - generate boxes (one list)
    - 8, 3, '.', '6', '.', '.', '.', '9', '8
    - Loop in increments of 3
      - Looping row += 3
    - Then I want to set first three cols as box1, next three box2
  - Check the digits are distinct
  - Return false if they are not

- Check distinct helper function
  - Create `digit_maps` variable
  - Loop through the rows/columns/box
    - Add the digits into digit_maps if not in dict
    - If it is - return false
  - Return true



"""

from typing import List

class Solution:
  def checkDistinct(self, digits: List[str]) -> bool:
    digit_maps = {}
    for digit in digits:
      if digit in digit_maps and digit != '.':
        return False
      else:
        digit_maps[digit] = 1
    return True

  def generateBoxes(self, board: List[List[str]]) -> List[List[str]]:
    results = []
    for row in range(0, 9, 3):
      for col in range(0, 9, 3):
        results.append(board[row][col:col+3] + board[row+1][col:col+3] + board[row+2][col:col+3])
    return results

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Check rows & cols on one loop
    for idx, row in enumerate(board):
      col = [row[idx] for row in board]
      if (self.checkDistinct(row) == False or self.checkDistinct(col) == False):
        return False

    for box in self.generateBoxes(board):
      if not self.checkDistinct(box):
        return False

    return True


sol = Solution()

# print(sol.checkDistinct(["5","3","3",".","7",".",".",".","."])) # false
# print(sol.checkDistinct(["5","3","2",".","7",".",".",".","."])) # true



board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board)) # true


board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board2)) # false
