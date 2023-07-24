
"""

Problem
-------------
Input: strings `s` and `t`
Output: string
  - gcd of s and t
  - t divides s if and only if `s = t + ... + t`

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

Algorithm Take 1
--------------
1. Loop through `str2` backwards
  - Find current_substring - str2[:idx]
  - Declare new variable called
  - while len(str1) > len(str)

"""

class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    pass
