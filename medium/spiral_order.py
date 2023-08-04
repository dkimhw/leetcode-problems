
"""
https://leetcode.com/problems/spiral-matrix/

Problem
------------
Input: matrix m x n [ [], [], [] ]
Output: array
  - elements are listed in spiral order from the input matrix

Example
-------------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Walkthrough
--------------

So it seems like you move in one direction until you cannot
And pattern is:
[right, down, left, up]

Then check if you can keep going in a direction for example right
If you cannot then switch to down if you can

Algorithm
---------------
1. Create variable `result`
2. while matrix is not empty (this needs to be expanded a little bit)
  2a. Loop over directions array [right, down, left, up]
  2b. Go through the elements in that direction & append to result (needs to be expanded) until you cannot go in that direction
    - expand on what elements are in that direction
    - replace element we visited as 'visited'
  2c. continue to the next direction
3. Return result

2b Expand
---------------
Notes:
  - I think we need some way to know where we currently are in the matrix
    - Then based on that & the direction we are currently on we can identify the elements that need to be visited
    - For example, if we are [0, 3] then we can use the 3 to go down or retrieve all column values in 3
  - Either pop or keep track of which locations you already visited or mark it as 'visited'

  1. Current location logic
    - declare current_loc = [0, 0]
    - as you move forward left/right/up/down - increase corresponding index
  2. Need logic by using current location & direction to return a list of elements that we need to visit
    - update current location
    - mark those elements in matrix as 'visited'
    - logic:
      - if "left" / "right"
        - take current_loc[0] and return the row
        - append elements not marked as 'visited'
        - update current_loc[0] += len(matrix[0])
      - if "up' / "down"
        - take current_loc[1] and return the col (bit more complicated)
        - append elements not marked as 'visited'
        - update current_loc[1] += len(matrix)

Two Problems
-----------------
1. Dealing with visited_cnt
2. Issue of updating current_loc
  - goes back to [0, 0]

"""
from typing import List
class Solution:
  def getColumn(self, matrix: List[List[int]], colIdx: int) -> List[int]:
    result = []
    for row in matrix:
      result.append(row[colIdx])
    return result

  def updateColumn(self, matrix: List[List[int]], colIdx: int) -> List[int]:
    for row in matrix:
      row[colIdx] = 'visited'

  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = []
    directions = ['right', 'down', 'left', 'up']
    current_loc = [0, 0]
    visited_cnt = 0
    m_x_n = len(matrix) * len(matrix[0])

    while visited_cnt < m_x_n: # come back & expand on this
      for direction in directions:
        if direction in ['right', 'left']:
          curr_row = matrix[current_loc[1]]
          curr_row = list(filter(lambda el: el != 'visited', curr_row))
          if direction == 'left':
            curr_row.reverse()
          # update the matrix
          matrix[current_loc[1]] = ['visited'] * len(matrix[0])

          # update variables

          if current_loc[0] == 0 and current_loc[1] == 0:
            current_loc[0] += len(matrix[0]) - 1
          elif direction == 'left':
            current_loc[0] -= len(curr_row)
          else:
            current_loc[0] += len(curr_row)

          visited_cnt += len(curr_row)

          result += curr_row
          if visited_cnt >= m_x_n:
            break

        elif direction in ['down', 'up']:
          # print(direction, ": ", current_loc)
          curr_col = self.getColumn(matrix, current_loc[0])
          curr_col = list(filter(lambda el: el != 'visited', curr_col))
          if direction == 'up':
            curr_col.reverse()

          # update the matrix
          self.updateColumn(matrix, current_loc[0])

          # update variables
          visited_cnt += len(curr_col)

          if direction == 'up':
            current_loc[1] -= len(curr_col)
          elif direction == 'down':
            current_loc[1] += len(curr_col)

          result += curr_col

          if visited_cnt >= m_x_n:
            break
      # break
    # print("current_location", current_loc)
    # print("matrix", matrix)
    # print("visited_cnt", visited_cnt)
    # print("m x n = ", len(matrix) * len(matrix[0]))

    return result


class SolutionAlt:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
    direction = 1 # Start off going right
    i, j = 0, -1
    output = []
    while m*n > 0:
      for _ in range(n): # move horizontally
        j += direction
        output.append(matrix[i][j])
      m-= 1
      for _ in range(m): # move vertically
        i += direction
        output.append(matrix[i][j])
      n-=1
      direction *= -1 # flip direction
    return output
