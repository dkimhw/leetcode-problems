

"""
https://leetcode.com/problems/isomorphic-strings/

Problem
-------------
Input: two strings `s` & `t`
Output: boolean (t/f)
  - true if two input strings are isomorphic
Notes:
  - isomorphic if characters in `s` can be replaced to get `t`


Examples
--------------

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Walkthrough
--------------
p -> t
a -> i
e -> l
r -> e

First it looks like we need to create the mapping - dictionaries definitely

ppaper title

Convert to:
paer tile


We can loop over `s` and replace the characters with the mapping values
Then compare `s` against this newly replaced character
  - if not equal - return false
  - if equal - return true

Algorithm
--------------
1. Create helper function that removes duplicate characters and returns a new string
  - create an empty string
  - loop through input string
    - if given char in empty string - don't append
    - else append
2. Call helper function twice
3. If len between these two are different - return false
4. Loop through the s_unique & create mapping
  - create dict called `char_map`
  - for each index:
    - char_map[s_unique[idx]] = char_map[t_unique[idx]]


"""

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    def unique_char_string(text: str):
      result = ""
      for idx in range(len(text)):
        curr_char = text[idx]
        if curr_char not in result:
          result += curr_char
      return result

    s_unique = unique_char_string(s)
    t_unique = unique_char_string(t)

    if len(s_unique) != len(t_unique):
      return False

    char_map = {}
    for idx in range(len(s_unique)):
      char_map[s_unique[idx]] = t_unique[idx]

    # convert the s
    converted_str = ""
    for idx in range(len(s)):
      converted_str += char_map[s[idx]]

    return converted_str == t
