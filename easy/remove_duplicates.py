
"""
PEDAC
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Input: String s consisting of lowercase letters
Output: String
  - this string contains no duplicate letters (i.e. adjacent and equal)

Examples

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Input: s = "azxxzy"
Output: "ay"

abbaca

abcdefghhhbbbzxy

abcdefgbbbzxy

index 7 - deleted 3
Do we just subtract by 1

Attempt Algorithm 1:
- Loop through string `s`
  - For each character - check if next series of elements are of the same character
    - Helper function
    - Given a starting index and string
      - find the number of characters after the given index that are the same
      - so if I give "aaaa" and 0 I would expect 3
    - it's always two adjacent
  - If it is, delete those characters in place
  - Move the index by 1
  - Then continue loop through the new shortened 's'



"""


class Solution:
  def findSameCharacters(self, s: str, start_idx: int) -> int:
    curr_idx = start_idx + 1
    result = 0
    if curr_idx < len(s) and s[start_idx] == s[curr_idx]:
      result += 1
    return result

  def removeDuplicates(self, s: str) -> str:
    counter = 0
    while counter < len(s):
      duplicate_characters = self.findSameCharacters(s, counter)
      if duplicate_characters > 0:
        s = s[:counter] + s[counter + duplicate_characters + 1:]
        if counter >= 1:
          counter -= 1
      else:
        counter += 1
    return s


sol = Solution()
print(sol.findSameCharacters("aaaa", 0))
print(sol.removeDuplicates("abbaca")) # ca
print(sol.removeDuplicates("azxxzy")) # ay
print(sol.removeDuplicates("abcdefghhhbbbzxy")) # abcdefgzxy
print(sol.removeDuplicates("aababaab")) # ba
print(sol.removeDuplicates("abbaca")) # ca
print(sol.removeDuplicates("aaaaaaaaa")) # a
