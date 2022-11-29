
"""
Input: array of nums
Output: Integer
  - the largest permieter of a triangle
  - If it is not possible to form a triangle (non-zero area) - return 0
  - What is the formula for calculating an area of a triangle
    - Use Heron's formula
Edge Case:
  - `nums` can have more than three elements

Test Cases

print(sol.largestPerimeter([2,1,2])) # 5
print(sol.largestPerimeter([1,2,1])) # 0

s = 2
sqrt(2 * (2-1) * (2 - 2) * (2 - 1))

Algorithm
1. Reorder the array from greatest to lowest
2. For each group of three elements:
  3. Check the area of the triangle - if it's zero then return 0
  4. Else: sum up the elements in array and return that value

[3, 2, 3, 4]
[4, 3, 3, 2]
"""
from typing import List
import math

class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    copy_nums = nums[:]
    copy_nums.sort(key = lambda x: x, reverse = True)
    for idx in range(len(copy_nums)):
      if idx + 2 < len(copy_nums) and copy_nums[idx + 1] + copy_nums[idx + 2] > copy_nums[idx]:
        return sum(copy_nums[idx:idx+3])
    return 0

sol = Solution()
# print(sol.largestPerimeter([2,1,2])) # 5
# print(sol.largestPerimeter([1,2,1])) # 0
# print(sol.largestPerimeter([3, 2, 3, 4])) # 10

# print(sol.largestPerimeter([3,6,2,3])) # 8
print(sol.largestPerimeter([1,2,2,4,18,8]))
