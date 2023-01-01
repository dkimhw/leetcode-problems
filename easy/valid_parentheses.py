
"""
https://leetcode.com/problems/valid-parentheses/

Input: string of parenthese (i.e. (), {}, [])
Output: boolean
  - true if `s` has valid parentheses
  - else false

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "( ()()[][()] )"
Output: true

Input: s = "(()[)"
Output: false

(,(,),[,)

Input: s = "(())"
Output: false

(, (, ), )


"""

class Solution:
    def isValid(self, s: str) -> bool:
