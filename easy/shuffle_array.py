
"""

Problem
------------------

Input: array of nums
  - [x1,x2,...,xn,y1,y2,...,yn]
Output: array of nums
  - shuffled array
  - [x1,y1,x2,y2,...,xn,yn]


Example
------------------

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]


Algorithm
------------------
1. Create results = []
2. Loop from 0 to n
  - Append to results
    - nums[idx]
    - nums[idx + n]
3. Return results

"""
from typing import List

class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    results = []
    for idx in range(n):
      results.append(nums[idx])
      results.append(nums[idx + n])
    return results
