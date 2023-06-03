
"""

Problem:
----------------
Input: array of strs (same length)
Output: int
  - # of cols you delete
  - What determines what you need to delete?
    - Convert the array into a matrix
    - Each column that is not lexicographically sorted --> delete

Examples:
----------------

Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.


Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.

Walkthrough:
----------------

Attempt 1:
- Go through each array and rearrange it
[[z, w, t], [y, v, r], [x, u, r]] O(n)
- Then loop through that and check if it is sorted correctly O(n) * O(n log n)

Attempt 2:
- Create a result variable
- Loop through the array:
  - Put z, w, t in:
  [[z], [w], [t]]
  - Next iteration, before putting them into respective subarrays
    - compare the last element with the element you are putting in
      - if it's not greater or equal then we know that it's not sorted lexicographically
      - increment result variable
  - O(n * k)

I think instead of saving them in arrays - we can jump do a nested loop

Algorithm:
----------------
1. Create a result variable = 0
2. Loop through the length of the string (k)
  - Loop through `strs` - index of jdx
    - For each `k` - compare the characters at position k for elements at jdx and jdx - 1
      - If at any point in that loop it's out of order (curr index < prev index)
        - break and increment result+=
      - else:
        - keep looping
3. Return result


"""
from typing import List

class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    result = 0
    k = len(strs[0])
    for idx in range(0, k):
      # print(idx)
      for jdx in range(1, len(strs)):
        # print(strs[jdx][idx])
        if strs[jdx][idx] < strs[jdx - 1][idx]:
          result += 1
          break
    return result
