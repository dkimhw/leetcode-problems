
"""

Understand the Problem
------------------------------

Input: integer
  - indicates how many versions you have
Output: integer
  - find the first bad version number since all versions after this will be bad


Examples
------------------------------
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Walkthrough
------------------------------
You have access to isBadVersion() function that will tell you whether a particular version is bad
or not

O(n) is brute force right. It's the same O(n) but looping starting from `n`
will save api calls as long as the bad version is not on version 1

isBadVersion() for example, calling it on 4 afterward will always return true right?
  - This is an ordered array
  - Can we use divide and conquer method?

Go to the midpoint
  - if this is not bad then we need to check the upper array
  - take the midpoint there - if it's bad - need to check the lower array to see if there is a version that is lower




Algorithms
------------------------------

1. Create a left & right pointer; result variable
2. While left < right, loop
  - Calculate midpoint
  - If this midpoint is bad:
    - set right = midpoint - 1
    - set result = midpoint
  - If this midpoint is good:
    - set left = midpoint + 1
3. Return result


"""

from typing import List

def isBadVersion(n: int) -> bool:
  if n in [4, 5]:
    return True
  else:
    return False

class Solution:
  def firstBadVersion(self, n: int) -> int:
    left = 1
    right = n
    result = None

    while left <= right:
      midpoint = (left + right) // 2
      is_mid_point_bad = isBadVersion(midpoint)
      print("midpoint", midpoint)
      if is_mid_point_bad:
        # print("hello", is_mid_point_bad)
        right = midpoint - 1
        result = midpoint
      else:
        left = midpoint + 1

    return result


sol = Solution()
print(sol.firstBadVersion(5))
#print(sol.firstBadVersion(1))

[1, 2, 3, 4, 5]
