
"""

Problem

  Input: Two sorted arrays (elements are integers)
  Output: One array with elements from both arrays (sorted asc)

Examples

  Input: [1, 2, 3] [1, 4, 5, 6]
  Output: [1, 1, 2, 3, 4, 5, 6]


Algorithm:
  - create a `result` variable
  - Start with idx1 and idx2 to track the current index position while looping through both arrays
  - while idx1 < len(arr1) and idx2 < len(arr2)
    - if arr1[idx1] < arr2[idx2] then append arr1[idx1] to result and increment idx1
    - else: do the opposite
  - if len of either of the array is > 0
    - concat the remaining val into `result`
  - return `result`


"""
from typing import List

class Solution:
  def merge_sorted_array(self, arr1: List[int], arr2: List[int]):
    idx1 = 0
    idx2 = 0
    result = []
    while idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] <= arr2[idx2]:
        result.append(arr1[idx1])
        idx1 += 1
      elif arr2[idx2] < arr1[idx1]:
        result.append(arr2[idx2])
        idx2 += 1
    if idx1 < len(arr1):
      result += arr1[idx1:]
    elif idx2 < len(arr2):
      result += arr2[idx2:]

    return result


sol = Solution()
print(sol.merge_sorted_array([1, 2, 3], [1, 4, 5, 6])) # [1, 1, 2, 3, 4, 5, 6]
