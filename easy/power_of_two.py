
"""

https://leetcode.com/problems/power-of-two/

PEDAC

Input: integer `n`
  - can be negative
Output: boolean
  - true if `n` is a power of two
  - else false

Example:

Input: n = 1
Output: true
Explanation: 2^0 = 1

Input: n = 16
Output: true
Explanation: 2^4 = 16

Input: n = -16
Output: true
Explanation: 2^4 = 16



Input: n = 3
Output: false


0, 1, 2, 3, 4, ...

n/2 or O(n)

Algorithms:
- set compare_n = abs(n), current_n = 1
- start a while loop
  - condition: current_n < n
  - if current_n * 2 is == n:
    - breal
  - set current_n *= 2
- if current_n == n:
  - return true
  - else: return false

16

0: 1
1: 2
2: 4
3: 8
4: 16

-16



"""

# class Solution:
#   def isPowerOfTwo(self, n: int) -> bool:
#     current_n = n
#     # edge case
#     if current_n == 0:
#       return False

#     while current_n != 0:
#       # edge case
#       if current_n == 1 or current_n == -1:
#         break

#       if current_n % 2 == 0:
#         current_n /= 2
#       else:
#         return False
#     return True

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    compare_n = abs(n)
    current_n = 1
    if current_n == 0:
      return False

    while current_n < compare_n:
      if current_n == n:
        break
      current_n *= 2

    if (current_n == n):
      return True
    else:
      return False


sol = Solution()
print(sol.isPowerOfTwo(3))
