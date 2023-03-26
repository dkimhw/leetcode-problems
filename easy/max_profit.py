
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem
---------------
Inputs: array of prices
  - prices = [7,1,5,3,6,4]
Outputs: integer
  - maximum profit that is possible give prices


Example
---------------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Algorithms
---------------
O(n^2) is fairly easy to implement

Is there an O(n) solution?
1. Loop through the array
  - keep track of the current lowest price
  - keep track of current max profit; initial value at 0
  - if you find a bigger profit - replace that value
    - max(curr_price - low price tracked, max profit)
  - if you find a lower price - replace that value
2. return max profit

"""

from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    low_price = prices[0]
    max_profit = 0
    for idx in range(len(prices)):
      max_profit = max(prices[idx] - low_price, max_profit)
      low_price = prices[idx] if prices[idx] < low_price else low_price

    return max_profit
