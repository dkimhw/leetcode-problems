
"""
https://leetcode.com/problems/roman-to-integer/

Input: string in roman numerals
Output: integer calculated from the roman numerals

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


Examples:

Input: s = "III"
Output: 3
Explanation: III = 3.


Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Algorithm:
  - Create a map of roman char to int
  - Create variable result = 0
  - Loop through the roman numeral string
    - if the next val is > than the current val
      - take the next val and subtract it from current val
      - move index forward by 2
    - else
      - take the val returned from map and add it to result
      - move index forward by 1
"""


class Solution:
  def convertSingleRomanChar(self, s:str) -> int:
    roman_to_int_val_map = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    if s in roman_to_int_val_map:
      return roman_to_int_val_map[s]
    return None

  def romanToInt(self, s: str) -> int:
    result = 0
    idx = 0
    while idx < len(s):
      curr_val = self.convertSingleRomanChar(s[idx])
      next_val = self.convertSingleRomanChar(s[idx + 1]) if idx + 1 < len(s) else None

      if next_val and next_val > curr_val:
        result += next_val - curr_val
        idx += 2
      else:
        result += curr_val
        idx += 1
    return result

sol = Solution()
print(sol.romanToInt('III'))
print(sol.romanToInt("MCMXCIV"))
