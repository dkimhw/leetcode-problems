

"""

https://leetcode.com/problems/maximum-subarray/description/

Input: nums (array of integers)
Output: integer
  - sum of the largest subarray (cannot be reordered - ordering of the elements matter)
Questions:
  - subarray is continous set of elements subarray subset of nums
  - are we expecting empty arrays? no 1 <= nums.length <= 105

Example:

  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: The subarray [4,-1,2,1] has the largest sum 6.

  Input: nums = [5,4,-1,7,8]
  Output: 23
  Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

  Input: nums = [5,4,-30,7,8]
  Output: 15
  Explanation: The subarray [7,8] has the largest sum 15.

O(n^2) brute force
greatestVals = [9, 4, -15, 15, 8] - take the max of these

Is there a more efficient approach?

[1, 1, -2] -> 1 + 1 -2
iteration 0: maxSum = 1
iteration 1: maxSum = 2
iteration 2: maxSum = 2 because 2 -2 = 0 so still 2

[10, -2, -2, 10]
iteration 0: maxSum = 10, currSum = 10
iteration 1: maxSum = 10, currSum = 8
iteration 2: maxSum = 10, currSum = 6
iteration 3: maxSum = 16, currSum = 16

[-2, 10, -2, -2, 10]
iteration 0: maxSum = -2, currSum = -2

Do we want to reset currSum when there is a value greater than maxSum

 [-2,1,-3,4,-1,2,1,-5,4]
 iteration 3: maxSum = 1, currSum = -2
 iteration 4: maxSum = 4, currSum = 4

Approach 1:
  - create `max_sum = first element`, `curr_sum = first element`
  - Loop through `nums` starting from index 1
    - Is current element > max_sum:
      then set max_sum = current element
      then set curr_sum = first element
      continue to next element
    - else:
      curr_sum += current_element
      then set max_sum = max of curr_sum and max_sum
  - return max_sum



I know there is a divide and conquer algorithm that I remember studying while, while back
in my algos class but I don't quite remember that.
"""
from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    try:
      max_sum = nums[0]
      curr_sum = nums[0]
      for idx in range(1, len(nums)):
        curr_element = nums[idx]
        # print(idx, '-', curr_sum, '-', max_sum)
        if curr_element >= 0 and curr_sum + curr_element < curr_element:
          max_sum = max(curr_element, max_sum)
          curr_sum = curr_element
        elif curr_element < 0 and curr_element > curr_sum:
          max_sum = max(curr_element, max_sum)
          curr_sum = curr_element
        else:
          curr_sum += curr_element
          max_sum = max(max_sum, curr_sum)

      return max_sum
    except IndexError:
      return IndexError


sol = Solution()
print(sol.maxSubArray([-2, 10, -2, -2, 10])) # 16
print(sol.maxSubArray([5,4,-1,7,8])) # 23
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(sol.maxSubArray([1,2])) # 3
print(sol.maxSubArray([-1,-2])) # -1
print(sol.maxSubArray([-2, -1])) # -1
print(sol.maxSubArray([-1, 0])) # 0
print(sol.maxSubArray([-1,-1,-2,-2])) # -1
print(sol.maxSubArray([1,-2,0])) # 1
