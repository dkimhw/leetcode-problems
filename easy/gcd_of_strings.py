
"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

Problem
-------------
Input: strings `s` and `t`
Output: string
  - gcd of s and t
  - t divides s if and only if `s = t + ... + t`
Notes:
  - is str1 always larger than str2

Examples
--------------

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Algorithm Walkthrough
--------------
- Take str2; start with the full string i.e. ABAB
- If the concatenation fails - i.e. ABAB + ABAB != ABABAB
- Then we can take ABA - repeat
- Then take AB - successful

Algorithm Take 1 - O(n * (m + n)) or O(n^2)
--------------
1. Find the smaller string
2. Loop through smaller string backwards (because it is gcd)
3a. For each iteration
  - Find current_substring - str2[:idx]
  - Declare new variable called `output`
  - while len(str1) > len(output):
    - output += current_substring
    - compare str1[:len(output)] == output[:len(output)]
      - if false: break
      - else: continue
  - if str1 == output: return current_substring
3b. For each iteration
  - Do the same above for the smaller string from 3a
4. Return ""


Algorithm Take 2 - O(min(m,n)⋅(m+n))
1. Find the shorter string among str1 and str2, without loss of generality, let it be str1.
2. Start with base = str1, and check if both str1 and str2 are made of multiples of base.
    - If so, return base.
    - Otherwise, we shall try a shorter string by removing the last character from base.
3. If we have checked all prefix strings without finding the GCD string, return "".

Time complexity:
We checked every prefix string base of the shorter string among str1 and str2, and verify if both strings are made by multiples of base. There are up to min⁡(m,n) prefix strings to verify and each check involves iterating over the two input strings to check if the current base is the GCD string, which costs O(m+n). Therefore, the overall time complexity is O(min(m,n)⋅(m+n)).


"""

class SolutionTest:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    if len(str1) >= len(str2):
      longerStr = str1
      smallerStr = str2
    else:
      longerStr = str2
      smallerStr = str1

    for idx in reversed(range(len(smallerStr))):
      current_substring = smallerStr[:idx + 1]
      output1 = ""
      output2 = ""

      while len(longerStr) > len(output1):
        output1 += current_substring
        if longerStr[:len(output1)] == output1[:len(output1)]:
          continue
        else:
          break

      while len(smallerStr) > len(output2):
        output2 += current_substring
        if smallerStr[:len(output2)] == output2[:len(output2)]:
          continue
        else:
          break

      if longerStr == output1 and smallerStr == output2:
        return current_substring
    return ""

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def valid(k):
      if len1 % k or len2 % k:
        return False

      n1, n2 = len1 // k, len2 // k
      base = str1[:k]
      return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len1, len2), 0, -1):
      if valid(i):
        return str1[:i]

    return ""
