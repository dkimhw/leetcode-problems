
"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

Problem
------------
Inputs: array of integers
Output: boolean
  - true if input arr can be arranged in arithmetic progression
  - arithmetic progression is where diff between any two consecutive elements is the same



Examples
------------

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

[2, 4, 4, 2]

[4, 2, 4, 2] --> this would return true but this is arithmetic seq
meaning it must be sorted from lowest to highest or highest to lowest

One way to solve this would be to sort array O(n log n)
Then check the first two elements - find `diff`
Loop through the array to check if the diff btwn the elements is == `diff`

Another way is that we don't need to sort this - if we find the min value
and max value

We know that max - min is the sum of all the differences between the sequences so you can
find the diff as (max - min) / (n - 1)

Then finally, the difference between each element and min value should be divisible by diff
If not return false

Algorithm:
1. Find max, min
2. Calculate `diff`
3. Create a variable called nums_checked = []
4. Loop through `nums` and check if
  - (max - nums[i]) % diff == 0
  - if false - return false
  - else: append to nums_checked(el)
5. Return true if len(`nums_checked`) == len(`arr`)

"""
from typing import List

class Solution:
  def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    min_val, max_val = min(arr), max(arr)
    diff = (max_val - min_val) // (len(arr) - 1)

    # edge conditions
    if max_val - min_val == 0: return True
    if (max_val - min_val) % (len(arr) - 1) != 0: return False
    set_arr = set(arr)
    if len(set_arr) < len(arr):
      return False

    for el in arr:
      curr_val = (el - min_val) % diff if diff != 0 else 0
      if curr_val != 0:
        return False

    return True
