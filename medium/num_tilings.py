
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
* Fully covered board: All tiles on board are covered by a domino or a tromino.
* Partially covered board: Same as a fully covered board, except leave the tile in the upper-right corner (the top row of the rightmost column) uncovered. Note, a board with only the lower-right corner uncovered is also considered "partially covered." However, as we will discover soon, we do not need to keep track of which corner is uncovered because of symmetry.
* `f(k)`: The number of ways to fully cover a board of width k.
* `p(k)`: The number of ways to partially cover a board of width k.
  - Because of trominos
* We can determine the number of ways to fully or partially tile a board of width k by considering every possible way to arrive at f(k) or p(k) by placing a domino or a tromino.
  - From f(k−1) we can add 1 vertical domino for each tiling in a fully covered board with a width of k−1
  - From f(k−2) we can add 2 horizontal dominos for each tiling in a fully covered board with a width of k−2
  - From p(k−1) we can add an L-shaped tromino for each tiling in a partially covered board with a width of k−1.
  - f(k)=f(k−1)+f(k−2)+2∗p(k−1)
* p(k)
  - Adding a tromino to a fully covered board of width k−2 (i.e. f(k−2))
  - Adding a horizontal domino to a partially covered board of width k−1 (i.e. p(k−1))
  - p(k)=p(k−1)+f(k−2)

1. Start from `f(n)` and then dive all the way to the base cases, f(1), f(2), p(2)
2. Define subproblems
2. Recursion calls will use the results of subproblems and base cases to help us get the final result, f(n).
  - The stop condition for the recursive calls is when k reaches a base case (i.e. k<=2k <= 2k<=2). Values for the base cases will be directly returned instead of making more recursive calls.
    - f(1)=1
    - f(2)=2
    - p(2)=1
"""
from functools import cache

class Solution:
  def numTilings(self, n: int) -> int:
    MOD = 1_000_000_007

    @cache
    def p(n):
      if n == 2:
          return 1
      return (p(n - 1) + f(n - 2)) % MOD

    @cache
    def f(n):
      if n <= 2:
          return n
      return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

    return f(n)

sol = Solution()
print(sol.numTilings(3))
