
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




"""


class Solution:
    def romanToInt(self, s: str) -> int:
