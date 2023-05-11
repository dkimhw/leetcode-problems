
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Problem
-------------

Input: str of digits i.e. "23"
  - you will only get empty string or string of 2-9
Output: array
  - list of all possible letter combinations
Notes:
  - each digits (outside of 1) has a mapping to a list of letters
  - i.e. 2: [a, b, c]

Examples
-------------

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]



Algorithms
-------------

Attempt 1:
1. Create a dictionary mapping digit to list of letters
2. Create a variable called results = []
3. Create a helper recursion method takes (digits, curr combination, results, curr digit idx):
  - base case:
    - if len of curr comb === len of input digits - append to results
  - recurse:
    - pass in a new digit letter
4. Call recurion method
5. return `results`

"""

from typing import List

class Solution:
  digit_to_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
  }

  def letterCombinationsRecursionHelper(self, combination: str, currDigit: int, digits: str, results: List) -> str:
    if len(combination) == len(digits):
      if (combination != ''):
        results.append(combination)
      return
    for letter in self.digit_to_letters[digits[currDigit]]:
      self.letterCombinationsRecursionHelper(combination + letter, currDigit + 1, digits, results)


  def letterCombinations(self, digits: str) -> List[str]:
    results = []
    self.letterCombinationsRecursionHelper('', 0, digits, results)
    return results


# sol = Solution()
# print(sol.letterCombinations('23'))

sol = Solution()
print(sol.letterCombinations(''))
