
"""

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

Algorithm Take 1
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

sol_test = SolutionTest()
print(sol_test.gcdOfStrings("ABCABC", "ABC")) # ABC
print(sol_test.gcdOfStrings("ABABAB", "ABAB")) # AB
print(sol_test.gcdOfStrings("LEET", "CODE")) # ""
print(sol_test.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")) # TAUXX
print(sol_test.gcdOfStrings("ABABABAB", "ABAB")) # ABAB
