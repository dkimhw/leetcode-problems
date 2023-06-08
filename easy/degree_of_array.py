
"""
https://leetcode.com/problems/degree-of-an-array/


Understand the Problem
----------------------------------

Input: `nums` - array of numbers
Output: integer
  - length of the shortest subarray that has the same degree as `nums`
Notes:
  - degree --> maximum freq of nums
  - the subarray just needs to contain the number with the maximum freq (they don't have to be next to each other)


Examples
----------------------------------
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.


Walkthrough
----------------------------------

Brute force - generate all subarrays
  - loop through each subarray to check for the shortest subarray that has the right degree

First find the max freq number let's say 2
  - Then loop over the array again

  [1,2,2,3,1,4,2]
    - keep track of numOfTwoFound
    - when that hits 3 we can break and that's the subarray that we want right
    - keep track of the first two found and the last two we needed


Algorithm:
----------------------------------
1. Create variable `element_map`,  `degree`, `first_idx`, last_idx`, `cnt`, `min_subarray_size`
2. Loop through nums & find the degree
  - Use dicitionary - count up the elements
    - also keep track of: first index where it appeared & last index where it appeared
3. Find the degree
4. Loop through element_map
  - Calculate the subarray size by subtracting last_idx - first_idx + 1 for every element
  - Keep track of the smallest arr size for elements where the cnt matches the degree
  - Only update the smallest arr size if (last_idx - first_idx + 1) is not zero and 'cnt' == degree
5. Return result


Issues:
----------------------------------
- the big issue is when there are ties in most freq
- Instead of just keeping track of how frequently something showed up
  - need to track the first & last appreance for each element to calculate the shortest subarray
"""

from typing import List
from collections import Counter

class Solution:
  def findShortestSubArray(self, nums: List[int]) -> int:
    element_map = {}
    for idx, num in enumerate(nums):
      if num in element_map:
        element_map[num]['cnt'] += 1
        element_map[num]['last_index'] = idx
      else:
        props = {'cnt': 1, 'first_index': idx, 'last_index': idx}
        element_map[num] = props

    degree = 0
    for _, val in element_map.items():
      degree = max(degree, val['cnt'])

    min_subarray_size = float('inf')
    for _, val in element_map.items():
      curr_subarray_size = val['last_index'] - val['first_index'] + 1
      if curr_subarray_size != 0 and degree == val['cnt']:
        min_subarray_size = min(min_subarray_size, curr_subarray_size)

    return min_subarray_size
