"""

https://leetcode.com/problems/rotate-array/description/

Problem
  Input: nums - array of integers, k - integer
    - k is non-negative
    - k = num of times to rotate `nums`
  Output: array of integers (not a new array - in-place)
    - mutated - i.e. rotated right by k steps

Example
  Input: nums = [1,2,3,4,5,6,7], k = 3
  Output: [5,6,7,1,2,3,4]
  Explanation:
  rotate 1 steps to the right: [7,1,2,3,4,5,6]
  rotate 2 steps to the right: [6,7,1,2,3,4,5]
  rotate 3 steps to the right: [5,6,7,1,2,3,4]

  Input: nums = [-1,-100,3,99], k = 2
  Output: [3,99,-1,-100]
  Explanation:
  rotate 1 steps to the right: [99,-1,-100,3]
  rotate 2 steps to the right: [3,99,-1,-100]

Algorithms:
  - Loop up to < k times
    - In each loop: pop out the last value and move it to the beginning of the array
  - return `nums`

Alternative:
  - Slice the two

"""
from typing import List

"""
Brute Force

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    for idx in range(k):
      last_item = nums.pop()
      nums.insert(0, last_item)
    return nums
"""

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    a = [0] * n
    for i in range(n):
      # print("idx:", (i + k) % n)
      # print("nums[i]:", nums[i])
      a[(i + k) % n] = nums[i]
      # print("a: ", a)
    nums[:] = a

sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate([1,2,3,4,5,6,7], 3)
print(nums)
