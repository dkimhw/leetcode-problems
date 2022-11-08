
"""

Input: string
Output: integer (index of input string)
  - returns the index of the first non-repeating character


Input: s = "leetcode"
Output: 0 because l does not repeat

Input: s = "loveleetcode"
Output: 2 because v is the first character not to repeat in the string

Algorithm:

1. Create an empty ordered dictionary called charDict
2. for each character in string
  - add to charDict
3. Loop through charDict
  - return the character that didn't repeat first and break from loop
4. Find that character idx in string using findIndex

O(3n) -> O(n)

"""
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
      charDict = OrderedDict()

      for char in s:
        if char in charDict:
          charDict[char] += 1
        else:
          charDict[char] = 1

      non_repeat_char = ''
      for k, v in charDict.items():
        if v == 1:
          non_repeat_char = k
          break

      non_repeat_char_idx = s.index(non_repeat_char) if non_repeat_char != '' else -1
      return non_repeat_char_idx



sol = Solution()
print(sol.firstUniqChar("leetcode")) # 0
print(sol.firstUniqChar("aa"))
