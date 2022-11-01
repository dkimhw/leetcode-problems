"""

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Input: array of nums
Output: array
  - each element represents the cumulative sum of nums up to that point

Test Cases:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

The current i in running total - is previous value so r[i - 1] + nums[i]

Algorithm:

1. Create a `running_total` array
2. Loop over nums
  - if idx == 0 then append nums[idx]
  - if idx > 0 then append nums[idx] + running_total[idx - 1]
3. Return running_total
"""

from typing import List

class Solution:
  def runningSum(self, nums: List[int]) -> List[int]:
    running_total = []
    for idx in range(len(nums)):
      if idx == 0:
        running_total.append(nums[idx])
      else:
        running_total.append(nums[idx] + running_total[idx - 1])
    return running_total

sol = Solution()
print(sol.runningSum([1,2,3,4])) # [1,3,6,10]
print(sol.runningSum([1,1,1,1,1])) # [1,2,3,4,5]
