
"""

Input: nums (arr of integers)
Output: integer that repeated first
Questions/Edge cases
  - when there is no recurring element - return None

Examples:
  nums = [2,5,1,2,3,5,1,2,4]
  output: 2

  nums=[2,1,1,2,3,5,1,2,4]
  output: 1

  nums=[2,3,4,5]
  output: undefined

set would work here as well; just need to check that it exists.

Algorithm:
  - loop over nums
     - if the current element is in set
        - return current element
     - else add to set

"""
from typing import List

class Solution:
  def first_recurring_char(self, nums: List[int]) -> int:
    elements = set()
    for num in nums:
      if num in elements:
        return num
      else:
        elements.add(num)
    return None
