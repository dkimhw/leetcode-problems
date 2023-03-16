
"""
Implement an insertion sort

Problem
------------

Input: array of integers
Output: sorted array of integers (same array)

Example
------------
Input: [4, 2, 1, 3]
Output: [1, 2, 3, 4]

Compare the first two elements 4 & 2. Since 2 is smaller move 2 to the left
[2, 4, 1, 3]

Now compare 4 against 1 and 1 against 2 - since it's lower move to the left of 2
[1, 2, 4, 3]

Now compare 3 against 1 2 4 - move to the left of 4


Algorithm:
- loop through the array
  - for each idx:
    - loop from 0 to that idx:
      - swap position if element at idx is <
- return array
"""
from typing import List
class Solution:
  def insertionSort(self, nums: List[int]) -> List[int]:
    for idx in range(len(nums)):
      currEl = nums[idx]
      # print("idx: ", idx)
      for jdx in range(idx):
        comparisonEl = nums[jdx]
        if currEl < comparisonEl:
          # swap
          nums[jdx], nums[idx] = nums[idx], nums[jdx]
    return nums

sol = Solution()
print(sol.insertionSort([4, 2, 1, 3]))
