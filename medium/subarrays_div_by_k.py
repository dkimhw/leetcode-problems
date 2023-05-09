
"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Problem
---------------

Input: array of integers, k = integer
Output: integer
  - number of subarrays whose sum can be divided k
Rules:
  - A subarray is a contiguous part of an array.
  - [1, 2, 3] -> [2, 3] is a subarray


Example
---------------
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Input: nums = [5], k = 9
Output: 0


Brainstorm & Walkthrough
---------------
- It would be fairly trivial to do this using brute force
  - i.e. calculate all possible subarrays and save the sum - then loop through and count number of times k can be divided cleanly
- Calculating all possible subarrays and sums (requires two nested loops): O(n^2)

[1, 1, 1, 1]

k = 2

answer is 4

Since subarrays are sequential, we can keep track of the prefix sum. For example:
* 1: [1]
  - sum = 1;key =  1 % 2 = 1; currently no prefixsum of 1 that we can use to achieve 2 which can be divided by 2
  - The remainder here is 1 (which is what we need to be able to be divided by 2) so we add to prefixSum['1'] += 1
  - prefixSum = {0: 1, 1: 1}
  - result = 0
* 2: [1, 1]
  - sum = 2;key 2 % 2 = 0; there is a prefixSum['0'] === 1
    - We add to `result` the value at prefixSum['0']
  - Then we add to prefixSum['0'] += 1
  - prefixSum = {0: 2, 1: 1}
  - result = 1
* 3: [1, 1, 1]
  - sum = 3; key = 3 % 2 = 1; There is a prefixSum['1'];
    - We add to `result` the value at prefixSum['1']
  - Then we add to prefixSum['1'] += 1
  - prefixSum = {0: 2, 1: 2}
  - result = 2
* 4: [1, 1, 1, 1]
  - sum = 4; 4 % 2 = 0; There is a prefixSum['1'];
    - We add to `result` the value at prefixSum['1']
  - Then we add to prefixSum['1'] += 1
  - prefixSum = {0: 3, 1: 2}
  - result = 4

Algorithms
---------------
1. Create dict called `prefixSum`; create a variable called `sum`; create a variable called `result`
2. Add base case of prefixSum[0] = 1
3. Loop through input
  - Add current idx value to `sum`
  - for each iteration:
    - check if sum - k exists in `prefixSum`
      - if true: increase `result` by the value at that key
    - add the new key (this is the current sum) and set value to 1
4. Return `result`


"""

from typing import List
from collections import Counter

class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    prefixSum = Counter()
    prefixSum[0] += 1
    rsum = 0
    result = 0

    for num in nums:
      rsum += num
      key = rsum % k
      if key in prefixSum:
        result += prefixSum[key]
      prefixSum[key] += 1

    return result

sol = Solution()
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))
print(sol.subarraysDivByK([1,1,1,1], 2))
