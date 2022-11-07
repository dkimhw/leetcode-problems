
"""

Input: 2D array (array of arrays) and truck size - maximum # of boxes that can be on the truck (int)
  - each element i [numberOfBoxes_i, numberOfUnitsPerBox_i]
Output: Intger
  - maximum total number of units that can be put on the truck

Test Case:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Algorithm:
- Step 1: order the 2d array input by units per box
- Step 2: create variable results = 0; and curr_boxes = 0
- Step 3: for each element in the array
  - for loop based on number of boxes
    - if curr_boxes == truckSize: break
    - else:
      - increment curr_boxes += 1
      - increment results += units per box for that element

- Final Step: return results

"""
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
      def order_box (box):
        return box[1]

      boxTypes.sort(key = order_box, reverse = True)
      # print(boxTypes)
      result = 0
      curr_boxes_in_truck = 0
      for box in boxTypes:
        for i in range(box[0]):
          if curr_boxes_in_truck == truckSize:
            return result
          else:
            curr_boxes_in_truck += 1
            result += box[1]

      return result

sol = Solution()
print(sol.maximumUnits([[2,2],[3,1],[1,3]], 4)) # 8

sol = Solution()
print(sol.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)) # 91


sol = Solution()
print(sol.maximumUnits([[2,2]], 4)) # 4
