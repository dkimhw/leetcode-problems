"""
https://leetcode.com/problems/contains-duplicate-ii/

Problem:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: List of numbers
Output: boolean
  - return true if there are numbers with two distinct indices
  - where they are equal and their indexes are <= k

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Walkthrough:

Input: nums = [1,2,3,1], k = 3

{
  1: [0, 3]
}

O(n) - loop once create dictionary as you go and stop loop when we find that such pair exists

Algorithm:
- Create a dictionary called `elementIndices`
- Loop through `nums`
  - check if the current index against the array at the key of element and see if <= k
    - if yes - return True
  - add the current index of the element at key of element - if 1 and index = 3, add 3 to the array at 1
- At the end of the loop
  - Return False


"""

from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    elementIndices = {}
    for idx, val in enumerate(nums):
      if val in elementIndices:
        for jdx in elementIndices[val]:
          if abs(idx - jdx) <= k:
            return True
        elementIndices[val].append(idx)
      else:
        elementIndices[val] = [idx]
    return False


# sol = Solution()
# print(sol.containsNearbyDuplicate([1, 2, 3, 4, 4], 1))
