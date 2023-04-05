"""
https://leetcode.com/problems/house-robber/

Problem
--------------

Input: list of nums
Output: int
  - max amt that can be stolen without alerting police
Rules:
  - When is the police alerted?
    - if two adjacent houses were broken into on the same night - alerts police

Examples
--------------

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4. Cannot rob 2, 3 because they are adjacent

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


This feels like a dynamic programming problem solved using recursion

At 2: max(2, 0)
At 7: max(prev which is 2, current which is 7 + 0)
At 9: max(prev which is 7, current which is 9 + 2)
At 3: max(prev which is 11, current which is 3 + 7)

Algorithm:

1. Create a list called `cache`
2. Start a loop
  - for each idx:
    - cache[idx] = max(cache[idx - 1], cache[idx - 2] + nums[idx])
3. Return cache[-1]
"""

from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    cache = [0] * len(nums)
    print(cache)
    for idx in range(len(nums)):
      if idx == 0:
        cache[idx] = nums[idx]
      elif idx == 1:
        cache[idx] = max(nums[idx - 1], nums[idx])
      else:
        cache[idx] = max(cache[idx - 1], cache[idx - 2] + nums[idx])
    return cache[-1]


sol = Solution()
print(sol.rob([2,7,9,3,1]))
print(sol.rob([1,2,3,1]))
