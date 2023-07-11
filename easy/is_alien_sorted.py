
"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

Problem
-----------

Input:
  - array of words
  - order of alphabet
Output:
  - boolean whether the array of words is lexically sorted

Examples
-----------
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

So to able to check that it is sorted we would need to compare pair of words as we loop through the words array.

The other tricky part is that we need to set a "ranking" value for each of the characters in "order"
  - i.e. h < l
  - We can use the index values
  - Store it in a dictionary - then as we are comparing each character between two words where they are not equal
    - check the value - if the earlier word has the greater value then it's not ordered lexically.
    { 'h': 0, 'l': 1, 'a': 2 }


Algorithm
-----------
1. Generate a dictionary of characters in order with values as the index of the string seq
2. Loop through the `words` array
  - Loop through words[i]
    - Compare each character words[i][j] against the same character position of words[i+1][j]
    - If they are different:
      - check the index values to see if the value of char words[i][j] < words[i+1][j]
      - if yes: break
      - if no: return false;
    - If a words[i] is shorter than words[i + 1] then return true
3. Return true

"""

from typing import List

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    char_values = {}
    for idx in range(len(order)):
      char_values[order[idx]] = idx

    for idx in range(len(words)):
      curr_word = words[idx]
      if idx + 1 < len(words):
        for jdx in range(len(curr_word)):
            # condition to check if curr words is longer
            if (jdx >= len(words[idx + 1])):
              return False

            if curr_word[jdx] != words[idx + 1][jdx]:
              # print("curr word char", curr_word[jdx])
              # print("next word", words[idx + 1][jdx])
              if char_values[curr_word[jdx]] < char_values[words[idx + 1][jdx]]:
                break
              else:
                return False
    return True


sol = Solution()
print(sol.isAlienSorted(["hello","leetcode"],  "hlabcdefgijkmnopqrstuvwxyz")) # true
print(sol.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # false
print(sol.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # false
