
"""
https://leetcode.com/problems/kth-missing-positive-number/
Problem
------------------

Input: array of nums
Output: integer
  - represents the kth integer in an array of missing numbers
Notes:
  - missing numbers are numbers that do not appear in nums
  - assume k will === arr.length

Examples
------------------
Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Algorithm
------------------
1. Create variables: `missingNums`
2. Create a helper function that takes in two nums
  - currNum
  - startNum
  - Returns all the integers between those two points
3. Loop through nums
  - call helper function
  - concat to missingNums
4. Return missingNums[k]



"""

class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
    ar
