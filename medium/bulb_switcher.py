
"""
https://leetcode.com/problems/bulb-switcher/

Problem
------------
Input: n bulbs (integer)
Output: # of bulbs that are on (integer)


Example
------------

Input: n = 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.


Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 1


Algorithm O(n^2):
--------------
1. Create a n-size array of 0s
2. Loop n times
  - For each iteration:
    - toggle every i-th bulb
  - For example: 0th iteration - you toggle every bulb
3. return sum(arr)

"""

class Solution:
  def bulbSwitch(self, n: int) -> int:
    # edge cases:
    if n == 0:
      return 0
    elif n == 1:
      return 1

    bulbs = [1] * n
    for i in range(1, n):
      for j in range(len(bulbs)):
        if (j + 1) % (i + 1) == 0:
          bulbs[j] = 1 if bulbs[j] == 0 else 0
        # print(i, '-', bulbs)

    return sum(bulbs)

sol = Solution()
print(sol.bulbSwitch(3)) # 1
print(sol.bulbSwitch(2)) # 1
# print(sol.bulbSwitch(0))
# print(sol.bulbSwitch(1))
