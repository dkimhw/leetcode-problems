
"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


Problem
----------------

Input: array of unique integers
  - each element represent ith employee's salary
Output: float
  - average that does not include min & max of the input array


Example:
----------------
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

Walkthrough:
----------------
O(n log n)

sort:
[1000, 2000, 3000, 4000]

Then we know the min & max will be at 0 and -1 respectively so
salaries[1:len(salaries) - 1] is the sum that we want

Alternatively:
O(2n)

Loop salary - find min & max
Loop salary again - and only add up values that are not min & max


Algorithm:
----------------
1. Sort the salary arry
2. return salary[1: len(salary) - 1].sum() / len(salary) - 2


1.Loop through array
  - sum += el
  - check if el is < min
  - check if el is > max
2. return (sum - min - max) / (len(salary) - 2)

"""
from typing import List


class Solution1st:
  def average(self, salary: List[int]) -> float:
    # sort salart
    salary.sort()
    return sum(salary[1: len(salary) - 1]) / (len(salary) - 2)


import math
class Solution:
  def average(self, salary: List[int]) -> float:
    min = float(math.inf)
    max = float(-math.inf)
    sum = 0

    for el in salary:
      sum += el
      if el < min:
        min = el

      if el > max:
        max = el

    return (sum - min - max) / (len(salary) - 2)
