
"""

https://leetcode.com/problems/palindrome-number/

Problem:

Input: integer `x`
Output: boolean
  - true if `x` is palindrome else false

Example:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Algorithm:
- Turn integer into a string
- Create two pointers (one at start and at end) and start a loop:
  - start comparing the two digits and if they are different - break and return false
- return true
"""


class Solution:
  def isPalindrome(self, x: int) -> bool:
    str_x = str(x)
    left = 0
    right = len(str_x) - 1

    while left < right:
      if str_x[left] != str_x[right]:
        return False
      else:
        left += 1
        right -= 1
    return True

sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
