
"""

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
    - Compare each character against the same character position of words[i+1]
    - If words



"""

from typing import List

class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    pass
