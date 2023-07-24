
"""
https://leetcode.com/problems/merge-strings-alternately/


Problem
-------------

Input: Two string `word1` and `word2`
Output: New string
  - merge by alternating chars from word1 and word2
Notes:
  - if a string is longer than the other - append the additional letters onto the end of the merged string
  - Note that you start with char from word1

Example
-------------

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  abc
word2:  pqr
merged: apbqcr

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  ab
word2:  pqrs
merged: apbqrs

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Algorithm Walkthrough
-------------

Loop `word1`
  - alternate
  apbq
  - edge conditions
  - then if curr_idx == len(word1) -1 and curr_idx < len(word2)
    - append remaining word2 characters
  - then if curr_idx > len(word2) - 1
    - append remaining word1 characters

Algorithm
-------------
1. Create variable called `result`
2. Loop `word1` - for each idx
  - edge conditions
  - append to result word1[i]
  - append to result word2[i]

- Edge condition 1 (where word2 is longer)
  - if curr_idx > len(word1) -1 and curr_idx < len(word2)
    - append remaining word2 characters

- Edge condition 2 (where word1 is longer)
  - if idx > len(word2) - 1 and len(word1) > len(word2)

"""


class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    result = ''

    for idx in range(len(word1) + 1):
      if idx > len(word1) - 1 and idx < len(word2):
        result += word2[idx:]
        break
      elif idx > len(word2) - 1 and len(word1) > len(word2):
        result += word1[idx:]
        break

      if idx < len(word1):
        result += word1[idx]
        result += word2[idx]

    return result
