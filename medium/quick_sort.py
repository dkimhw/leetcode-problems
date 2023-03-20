
"""

Problem
-------------

Input: array of nums
Output: sorted array of nums


Example
-------------

Input: [4, 2, 6, 7, 10, 9]
Output: [2, 4, 6, 7, 9, 10]


Data Structures & Algos
-------------

- Pick a random pivot point
- For each recursion step:
  - Base case:
    - If arr.length === 1 then return arr because there is nothing to sort
  - Move all elements smaller than the pivot point to a lesser array
    - remove element
    - insert at 0 if smaller
  - Move all elements greater than the pivot point to a greater array
    - remove element
    - append if greater
  - Call 1st recursion with lesser array
  - Call 2nd recursion with greater array
  - Combine the result of both with the pivot idx between lesser and greater
  - return result

"""
from typing import List
import random

class Solution:
  def reorderElements(self, nums: List[int], pivotIdx: int) -> List[int]:
    lesser = []
    greater = []
    for idx in range(len(nums)):
      if pivotIdx == idx:
        continue

      if nums[idx] <= nums[pivotIdx]:
        lesser.insert(0, nums[idx])

      if nums[idx] > nums[pivotIdx]:
        greater.append(nums[idx])
    return lesser, greater

  def quickSort(self, nums: List[int]) -> List[int]:
    # base condition
    if len(nums) <= 1:
      return nums

    pivotIdx = random.randint(0, len(nums) - 1)
    lesser, greater = self.reorderElements(nums, pivotIdx)
    result = self.quickSort(lesser) + [nums[pivotIdx]] + self.quickSort(greater)
    #result += result

    print("result", result)
    return result



sol = Solution()
print(sol.reorderElements([4, 2, 6, 7, 10, 9], 3))
print(sol.quickSort([4, 2, 6, 7, 10, 9]))
