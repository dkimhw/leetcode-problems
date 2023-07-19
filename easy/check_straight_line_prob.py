"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/

Problem
------------------
Input: Array of arrays
  - each element is coordinate [x , y]
Output: Boolean
  - true if the coordinates are in a straight line
  - else false


Example
------------------

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


The coordinates are in a straight line if the slope is the same across the entire coordinates

Algorithm 1st Attemp
----------------------
1. Calculate the slope at idx == 0 & idx == 1
2. Loop through the coordinates
  - If the slope between idx & idx + 1 is the same as calc from step 1 continue
  - else - return false
3. Return true


Issue: Two points next to each other could be in a straight line technically but
for the coordinates to be straight I think it needs to have the same slope throughout
so if I take the beginning coordinate - check for the slope against the rest of the coordinate

[[0,0],[0,1],[0,-1]] --> this is technically
[[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]] --> the way I handle "x" value has to be different
"""
from typing import List

class Solution:

  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    def calc_slope(x, y):
      print("x", x)
      if x != 0:
        return y / x
      else:
        return None

    if len(coordinates) < 2:
      return True

    slope = calc_slope(coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1])

    for idx in range(1, len(coordinates)):
      curr_slope = calc_slope(coordinates[idx][0] - coordinates[0][0], coordinates[idx][1] - coordinates[0][1])
      print("curr_slope", curr_slope)
      if curr_slope == slope:
        continue
      else:
        return False
    return True


sol = Solution()
# print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
# print(sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
# print(sol.checkStraightLine([[0,0],[0,5],[5,5],[5,0]]))
# print(sol.checkStraightLine([[0,0],[0,1],[0,-1]]))
# print(sol.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]))
# print(sol.checkStraightLine([[1,-8],[2,-3],[1,2]]))
print(sol.checkStraightLine([[1,1],[2,2],[2,0]]))

# (-8 - -3) / (2 - 1) = -5 / 1 = -5
# (-3 - 2) / (1 - 2) = -5 / -1 = 5
# (0 - 1) / (2 - 1) = -1 / 1 = -1
