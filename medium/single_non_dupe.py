"""

Problem
--------------
Input: Sorted array of integers
  - only consists integers where every element appears exactly twice except for one element only happens once
Output: integer
  - returns the single element that appears only once
Notes:
  - Other reqs: Must run O(log n)

Examples
--------------

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10


So it's relatively straighforward to do this in O(n)
  - loop over each array
  - if the next variable is not the same - then we found the single non dupe element

divide & conquer?

So take a midpoint
1,1,2,3 ; 3 ; 4,4,8,8
- check left and right - if one of them checks
- continue

- next midpoint
4,4; 8; 8 - match 8 - so we would divide again

1,1; 2; 3 - non match so return



Algorithm
--------------

Main algo
1. Create a variable called `result`
2. Create a helper recurse function
  - takes (arr, result)
  - to be expanded below
3. Return `result`

Helper function*
1. Recursion base case
  - if arr.length <= 1 (cannot be divided any longer)
    - return
2. Create a midpoint from `arr`
3. Check the prev & next idx and compare to midpoint val
  - if one of prev or next is the same val then proceed to:
    4a. Create two new arrays to the left and right of the midpoint
    5a. Save the results to two variables
    6a. Only return the variable that is not None
  - if prev or next don't match
    4b. return val

"""
import math
from typing import List

class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    # base case
    if len(nums) <= 1:
      return

    # create midpoint
    midpoint = math.floor(len(nums) / 2)
    midpoint_val = nums[midpoint]
    next_val = nums[midpoint + 1] if midpoint + 1 < len(nums) else None
    prev_val = nums[midpoint - 1] if midpoint - 1 >= 0 else None

    if midpoint_val != next_val and midpoint_val != prev_val:
      return midpoint_val

    r1 = self.singleNonDuplicate(nums[0: midpoint])
    r2 = self.singleNonDuplicate(nums[midpoint:])

    if r1 != None:
      return r1
    elif r2 != None:
      return r2



sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11])) # 10
