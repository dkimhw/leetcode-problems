"""

https://leetcode.com/problems/move-zeroes/description/


Input: array of integers
Output: same array of integers but with zeroes at the end
  - rest of the elements maintain their relative order


Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

cnt = 0
idx = 0

while cnt < len(nums)
0 - since zero - splice and move to end, cnt+=1, idx - don't increment
0 - since not zero - continue, idx increment, cnt+=1
[1,0,3,12,0]
1 - since zero - splice, idx skip, cnt+=1 (cnt = 3)
[1,3,12,0,0]
1 - since zero - continue, idx increment, cnt+=1 (4)
[1,3,12,0,0]
2 - since zero - continue, idx increment, cnt+=1 (4)
[1,3,12,0,0]

Algorithms:
  - create `num_of_loops`, `current_idx`
  - while num_of_loops < len(nums)
    - if zero, splice the element and move to end of array
      - current_idx skip
      - num_of_loop += 1
    - if not, continue
      - current_idx += 1
      - num_of_loops += 1
  - return nums
"""
from typing import List

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    num_of_loops = 0
    current_idx = 0
    while num_of_loops < len(nums):
      if nums[current_idx] == 0:
        num_of_loops += 1
        nums.pop(current_idx)
        nums.append(0)
      else:
        current_idx += 1
        num_of_loops += 1
    return nums
