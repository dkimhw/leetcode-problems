
"""

Input: 9 x 9 array rep of sudoku board
Output: boolean
  - True if valid, False if not
  - Only the filled cells need to be validated according to the mentioned rules.
  - Unique digits in row, col, and 3 x 3 box


Algorithm:
- Loop through each row: check that the digits are distinct
  - Return false if they are distinct
- Loop through each col: check that the digits are disticnt
  - generate columns:
    - loop through the board
    - for each row:
      - append to the subarray that matches the current row index
      - so if we are at idx 3 - this is col 4 we append:
        - cols[3].append(row[3])
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

  def generateCols(self, board: List[List[str]]) -> List[List[str]]:
    cols = [[] for _ in range(9)]
    for row in board:
      for idx in range(len(row)):
        cols[idx].append(row[idx])
    print(cols)
    return cols

  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Check rows
    for row in board:
      if not self.checkDistinct(row):
        return False

    for col in self.generateCols(board):
      if not self.checkDistinct(col):
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
#print(sol.isValidSudoku(board)) # true


board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#print(sol.isValidSudoku(board2)) # false


def generateBoxes(board):
  boxes = [[] for _ in range(9)]
  # generate boxes every three rows
  for box_idx in range(0, len(board), 3):
    for row_idx in range(box_idx, box_idx + 3):
      for col_idx in range(0, 9, 3):
        # print(board[row_idx][col_idx:col_idx+3])
        boxes[row_idx].append(board[row_idx][col_idx:col_idx+3])
  return boxes





print(generateBoxes(board2))
