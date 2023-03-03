
"""
https://leetcode.com/problems/domino-and-tromino-tiling/editorial/

Problem:

Input: `n` integer value - shows the width of the board (2 x n board)
Output: integer value
  - number of different ways to create 2 x n board
Notes:
  - Since the answer may be very large, return it modulo 109 + 7.
  - Regular domino tile and Tromino tile
  - Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Examples:

Input: n = 3
Output: 5

Input: n = 1
Output: 1

Data Structures:
 2 x n array

Walkthrough 2 x 3:
1. Three dominoes lined up side by side vertically

Aglorithm (backtracking):
1. Create a board 2 x n
2. Create possible positions that a dominoe and tromino tile can take
3. Recurse:
  - Check if a position is possible - if yes - add it
  - Once a valid way is found, pop out the last tile place to return to previous board stat to try all remaining tile placement

Algorithm (DP):
1.
"""
import numpy as np

class Solution:
  def numTilings(self, n: int) -> int:
    board = np.zeros((2, n))
    print(board)

sol = Solution()
print(sol.numTilings(3))
