"""

Input: two strings
Output: boolean
  - if almost equivalent
Defintion:
  - "almost equivalent": diff btwn frequencies of a-z characters at most 3
  - So "a": 0 , "a": 4 - this would be not almost equivalent
Edge Cases:
  - What about empty strings? Always at least one char
  - If the character is uniquely available in one string (you would have to loop over both collections)

Example:

Input: word1 = "aaaa", word2 = "bccb"
Output: false
Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
The difference is 4, which is more than the allowed 3.

Input: word1 = "abcdeef", word2 = "abaaacc"
Output: true
Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
- 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
- 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
- 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
- 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
- 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
- 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

Algorithm O(n):

- Count each character freq for word 1 and word 2 using something like counter
- Loop over word1 counter and compare each character freq against word 2 counter and if diff is ever > 3, return false
- Else return true
"""

from collections import Counter

class Solution:
  def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    word1_count = Counter(word1)
    word2_count = Counter(word2)
    char_list = list(word1_count.keys()) + list(word2_count.keys())

    for char in char_list:
      word1_freq = word1_count[char] if word1_count[char] else 0
      word2_freq = word2_count[char] if word2_count[char] else 0
      if abs(word1_freq - word2_freq) > 3:
        return False
    return True

sol = Solution()
print(sol.checkAlmostEquivalent("aaaa", "bccb"))
