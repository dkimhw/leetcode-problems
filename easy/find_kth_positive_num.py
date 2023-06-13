
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
1. Create variables: `missing_nums`
2. Create a helper function that takes in two nums
  - currNum
  - startNum
  - Returns all the integers between those two points
3. First loop through the array nums to find all missing nums
  - call helper function
  - concat to missingNums
3. Loop while currK <= k
  - if the `missing_nums` length is less than k
  - loop and append to missing_nums until currK == k
4. Return missingNums[k]

Helper function:
1. Create output = []
2. Loop between start and end (passed in arguments)
  - append to output
3. return output

"""
from typing import List

class Solution:
  def findKthPositive(self, arr: List[int], k: int) -> int:
    missing_nums = []
    def findNumsInBetween(start: int, end: int):
      outputs = []
      for idx in range(start + 1, end):
        outputs.append(idx)
      return outputs

    # First loop through the
    for idx in range(len(arr)):
      currMissingNums = []

      # use zero if first index
      if idx == 0:
        currMissingNums = findNumsInBetween(0, arr[idx])
        if len(currMissingNums) > 0:
          missing_nums += currMissingNums
      else:
        currMissingNums = findNumsInBetween(arr[idx - 1], arr[idx])
        if len(currMissingNums) > 0:
          missing_nums += currMissingNums

    currK = len(missing_nums)
    last_positive_num = arr[-1]
    if (currK <= k):
      while currK <= k:
        last_positive_num += 1
        missing_nums.append(last_positive_num)
        currK += 1
    return missing_nums[k - 1]

# More optimal version of O(n)
class Solution2:
  def findKthPositive(self, arr: List[int], k: int) -> int:
      # if the kth missing is less than arr[0]
      if k <= arr[0] - 1:
          return k
      k -= arr[0] - 1

      # search kth missing between the array numbers
      for i in range(len(arr) - 1):
          # missing between arr[i] and arr[i + 1]
          curr_missing = arr[i + 1] - arr[i] - 1
          # if the kth missing is between
          # arr[i] and arr[i + 1] -> return it
          if k <= curr_missing:
              return arr[i] + k
          # otherwise, proceed further
          k -= curr_missing

      # if the missing number if greater than arr[-1]
      return arr[-1] + k
