

"""
Implement merge sort

Problem
-------------
Input: array of nums
Output: sorted array of nums


Example
-------------
Input: [4, 6, 3, 5, 2, 1]
Output: [1, 2, 3, 4, 5, 6]

Walkthrough
-------------
[4, 6, 3],[5, 2, 1]
[4, 6], [3], [5, 2], [1]
[4],[6],[3],[5],[2],[1]

[4, 6],[3],[2, 5],[1]

Algorithms
-------------
- Break condition - an array of element = 1 is already sorted
- Recursively divide `num` until break condition
  - For each recursion:
    - call recursively on left & right (we are constantly dividing the array until break condition)
    - call merge sorted array algo
      - you have two sorted arrays [1, 2] and [4, 5]
      - you take [1, 2] then 4, 5
- Return the result of merge sorted array algo
"""
from typing import List
import math

class Solution:
  def mergeSortedArr(self, arr1: List[int], arr2: List[int]) -> List[int]:
    sorted_list = []
    while len(arr1) > 0 and len(arr2) > 0:
      if arr1[0] <= arr2[0]:
        sorted_list.append(arr1.pop(0))
      else:
        sorted_list.append(arr2.pop(0))

    if len(arr1) > 0:
      sorted_list += arr1
    elif len(arr2) > 0:
      sorted_list += arr2

    return sorted_list

  def mergeSort(self, nums: List[int]) -> List[int]:
    if len(nums) == 1:
      return nums

    midpoint = math.floor(len(nums) / 2)
    left = nums[:midpoint]
    right = nums[midpoint:]
    print("left: ", left)
    print("right: ", right)

    return self.mergeSortedArr(
      self.mergeSort(left),
      self.mergeSort(right)
    )


sol = Solution()
print(sol.mergeSortedArr([1, 3, 5, 7], [2, 4, 6]))
print(sol.mergeSortedArr([7], [6]))

print(sol.mergeSort([4, 6, 3, 5, 2, 1]))
