
"""

Input: m x n integer grid
output: integer
  - wealth of the richest customer

Test Cases

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""
from typing import List

class Solution:
  def maximumWealth(self, accounts: List[List[int]]) -> int:
    result = 0
    for account in accounts:
      acct_sum = sum(account)
      result = max(acct_sum, result)

    return result



sol = Solution()
print(sol.maximumWealth([[1,2,3],[3,2,1]]))
