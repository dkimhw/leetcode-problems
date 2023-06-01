"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

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

[3,3,7,7,10,11,11]
1. Midpoint is 7
2. Check if there are partners to the left and right
  - there is one to the left
3. Note that once we remove the two partners: the odd side has the single num - so we want to search in [10, 11, 11]
  - discard the other array (basically binary search)
  [3, 3]; [10, 11, 11]
4. So we search [10, 11, 11]
  - midpoint is 11
  - check for partners left & right
  - remove [11, 11]
5. Left with 10


Algorithm
--------------

Main algo
1. Create two pointers starting at the start and end
2. Find midpoint - (start + end // 2)
3. Check if both halves are even (end + mid % 2  === 0)
4. Check partners left & right
  - if mid + 1 === mid
    - if halves are even: we want to move the start to mid + 2 because we only want to check the array to the right
    - else: we want to move the end to mid - 1
  - if mid - 1 === mid
    - if halves are even: we want to move the high to mid -2 because we only want to check the array to the left
    - else: we want to move the start to mid + 1 because we only want to check the array to the right

"""
import math
from typing import List

class Solution:

  def singleNonDuplicate(self, nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    while start < end:
      midpoint = (start + end) // 2
      halves_even = (end - midpoint) % 2 == 0

      if nums[midpoint + 1] == nums[midpoint]:
        if halves_even:
          start = midpoint + 2
        else:
          end = midpoint - 1
      elif nums[midpoint - 1] == nums[midpoint]:
        if halves_even:
          end = midpoint - 2
        else:
          start = midpoint + 1
      else: # could be the midpoint is the unique
        return nums[midpoint]
    return nums[start]


sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11])) # 10
