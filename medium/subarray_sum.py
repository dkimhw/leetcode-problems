
"""

https://leetcode.com/problems/subarray-sum-equals-k/

Input: Array of integers, integer
Output: Integer
  - count of all subarrays that equal to k
  - subarrays are continguous non-empty sequence elements

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

There is an O(n^3) solution

Is there something faster? O(n)

[1, 2, 3, 1, 2, 3, 1, 2, 3]
k = 6

sum = 1; cnt = 0 (sum - k) = -5
sum = 3; cnt = 0 (sum - k) = -3
sum = 6; cnt = 1 (sum - k) = 0
sum = 7; cnt = 1 (sum - 6) = 1
sum = 9; cnt = 1 (sum - 6) = 3
sum = 12; cnt = 1 (12 - 6) = 6
sum = 13
sum = 15 (18 -)
sum = 18 (18 - 6) = 12
"""

from typing import List
from collections import Counter

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    cnt = 0
    sum_arr = 0
    track_cum_sum = Counter()
    track_cum_sum[0] += 1
    for idx in range(len(nums)):
      sum_arr += nums[idx]
      if sum_arr - k in track_cum_sum:
        cnt += track_cum_sum[sum_arr - k]

      track_cum_sum[sum_arr] += 1
    return cnt
