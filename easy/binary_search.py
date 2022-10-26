
"""

Input: Array of integers `nums`, integer `target`
  - `num` is sorted in ascending order
Output: Index of the `target`
  - If target exists return index
  - else -1

Examples:

print(sol.search([-1,0,3,5,9,12,13], 9)) # 4
print(sol.search([-1,0,3,5,9,12], 2)) # -1


Algorithm:

- Step 0: Start while loop
- Step 1: Get the middle of the array using math.ceil
- Step 2: If middle element is target: return index, break while loop
- Step 3: If the middle element < target (i.e. 5 < 9)
  - Set the array that needs to be searched from middle + 1 to end
- Step 4: If the middle element > target (i.e. 10 > 9)
  - Set the array from 0 to middle - 1
- Step 5: Return -1


"""
from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    start_idx = 0
    end_idx = len(nums) - 1

    while start_idx <= end_idx:
      middle_idx = (start_idx + end_idx) // 2
      # print(start_idx, ' ', end_idx, ' ', middle_idx)
      if nums[middle_idx] == target:
        return middle_idx

      if nums[middle_idx] < target:
        start_idx = middle_idx + 1

      if nums[middle_idx] > target:
        end_idx = middle_idx - 1
    return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12,13], 9)) # 4
print(sol.search([-1,0,3,5,9,12,13], 13)) # 6
print(sol.search([-1,0,3,5,9,12,13], 0)) # 1
print(sol.search([-1,0,3,5,9,12], 2)) # -1


print(sol.search([5, 6], 6)) # 1
print(sol.search([5], 5)) # 0
print(sol.search([2,5], 2)) # 0
