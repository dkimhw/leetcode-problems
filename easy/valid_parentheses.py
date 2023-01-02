
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
(, [, {
), ], }

Input: s = "(]"
Output: false

Input: s = "( ()()[][()] )"
Output: true

Input: s = "(()[)"
Output: false

(,(,[
), )

Input: s = "(())"
Output: false

(, (
), )

Algorithm:
  - create parentheses stack
  - loop through string
    - if open parens - add to stack
    - if close parens
      - pop parenthese stack
      - compare - make sure the open and closed are valid i.e. ()
        - if not return false
  - else retur true
"""

class Solution:
  def isValid(self, s: str) -> bool:
    parentheses = []
    for char in s:
      if char in ['(', '[', '{']:
        parentheses.append(char)
      else:
        last_item = parentheses.pop()
        if last_item == '(' and char != ')':
          return False
        elif last_item == '[' and char != ']':
          return False
        elif last_item == '{' and char != '}':
          return False
    return True

sol = Solution()
# print(sol.isValid("(())")) # true
print(sol.isValid("(()[)")) # false
print(sol.isValid("(()()[][()])")) # true
