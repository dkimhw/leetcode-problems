"""

Input: String, Abbreviation
Output: Abbreviated String
  - A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
  - No leading zeroes are allowed in the abbreviation.

Test Cases:

Given: "substitution"
"s10n" ("s ubstitutio n")
"12" ("substitution")

Algorithm:
- Loop over string input
- If abbreviation char is a letter - compare it to the input string at the same index
  - If they are not equal - return False
- If abbreviation char is a number - check the next chars until we see a letter
  - Slice the input string from the current index to the current index + the number
  - If this is valid - then we can move on to the next char in the abbreviation
  - Logic to skip the next set of digits
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
      curr_word_idx = 0
      curr_abbr_idx = 0
      for idx in range(len(abbr)):
        char = abbr[idx]
        if curr_abbr_idx > idx:
          continue
        elif curr_word_idx > len(word) - 1:
          return False
        elif char.isalpha():
          if word[curr_word_idx] != char:
            return False
          else:
            curr_word_idx += 1
            curr_abbr_idx += 1
        elif char.isdigit():
          next_char = curr_abbr_idx
          while next_char < len(abbr) and abbr[next_char].isdigit():
            next_char += 1

          # Check leading zero
          if abbr[curr_abbr_idx] == '0':
            return False

          digit = int(abbr[curr_abbr_idx:next_char])
          if curr_word_idx + digit > len(word):
            return False
          else:
            curr_word_idx += digit
            curr_abbr_idx = next_char
      if curr_word_idx == len(word):
        return True
      else:
        return False

sol = Solution()
# print(sol.validWordAbbreviation("substitution", "s10n")) # True
# print(sol.validWordAbbreviation("internationalization", "i12iz4n")) # True
print(sol.validWordAbbreviation("hi", "2i")) # True
