
"""
https://leetcode.com/problems/buildings-with-an-ocean-view/


Input: array
  - n buildings in a line.
Output: array
  -  list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Test Cases

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

4 is higher than 2, 3, 1
3 is higher than 1
1 is the last so 0, 2, 3

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

ocean_views = [0]
if 2 is bigger than ocean_view[0] than remove zero index and add 2
[6, 4, 7] - get rid of 6, 4 from ocean_views array right
[7, 3, 4, 5, 6] - get rid of 3, 4, 5 since 6 is higher

Algorithm O(n^2):
- Create list called ocean_views
- Loop heights array
  - compare current_height against view in ocean_views
  - delete all that is lower than the height
  - append index of current height
- return ocean_views
"""
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
      ocean_views = []

      for idx, height in enumerate(heights):
        cnt = len(ocean_views) - 1 if len(ocean_views) > 0 else 0
        while True:
          # print(cnt, " - ", len(ocean_views))
          if cnt < len(ocean_views) and height >= heights[ocean_views[cnt]]:
            del ocean_views[cnt]
          else:
            break
          cnt -= 1
          if cnt < 0:
            break

        ocean_views.append(idx)
      return ocean_views



sol = Solution()
# print(sol.findBuildings([4,2,3,1]))
# print(sol.findBuildings([7, 3, 4, 5, 6])) # [0, 4]
print(sol.findBuildings([7, 3, 4, 5, 6, 8, 8, 6, 5])) # [6, 7, 8]
print(sol.findBuildings([7, 3, 4])) # [0, 2]
