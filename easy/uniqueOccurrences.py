
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Input: Arr
Output: Boolean
  - True if the number of occurrences of each value in the array is unique

Example:
arr = [1,2,2,1,1,3] # true

Algorithm:

- Intialize a dictionary
- Loop over array
- For each element, if in dictionary increment by 1 else set to 1
- Loop over dictionary - if there are same number of occurrences - return false

"""
from typing import List
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      cnt_occurrences = collections.Counter()
      for num in arr:
        cnt_occurrences[num] += 1
      vals = list(cnt_occurrences.values())
      len_list = len(vals)
      len_set = len(set(vals))

      return len_list == len_set


sol = Solution()
print(sol.uniqueOccurrences([1,2,2,1,1,3])) # true
print(sol.uniqueOccurrences([1,2])) # false
