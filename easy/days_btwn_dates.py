"""
https://leetcode.com/problems/number-of-days-between-two-dates/

Problem (understand the problem):
  Input: two dates
    - format: YYYY-MM-DD
  Output: integer
    - days between the two dates
  Questions
    - are the dates given in particular order - i.e. first argument is always > second argument?
      - no - then we subtract but must apply absolute value
    - are we able to use built in datetime modules in i.e. datetime in python?

Examples

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Algorithm:
- Convert each string dates into a date object
- Calcualte the delta in days between the two days
- Return the delta
"""
import datetime

class Solution:
  def daysBetweenDates(self, date1: str, date2: str) -> int:
    converted_date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    converted_date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    delta = abs(converted_date2 - converted_date1).days
    return delta
