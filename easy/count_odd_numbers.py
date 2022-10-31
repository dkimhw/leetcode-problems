"""

Input: two integers - low and high
Output: intger
  - # of odd integers btwn low and high

Test Cases:


Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].


Algorithm:

- Number of odd numbers => high - low / 2
- Need to account for cases if low or high is an odd - we need to add one in that scenario

"""

import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
      add_if_not_even = 1 if low % 2 != 0 or high % 2 != 0 else 0
      return math.floor((high - low) / 2) + add_if_not_even

sol = Solution()
print(sol.countOdds(3, 7)) # 3
