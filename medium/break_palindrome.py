
"""

https://leetcode.com/problems/break-a-palindrome/

Problem

  Input: string (assume always a palindrome)
  Output: string
    - lexicographically smallest string that breaks the palindrome input
    - if it's not possible to replace a character to break it - return empty string


Examples

  Input: palindrome = "abccba"
  Output: "aaccba"
  Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
  Of all the ways, "aaccba" is the lexicographically smallest.

  Input: palindrome = "a"
  Output: ""
  Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Quick Walkthrough

  Start from "a" and start from "a" (at the end of string)
  "a" === "a" but since replace 'a' with something like 'b' would result in a high lexicography - you don't want this
  We can change "b" to "a" and since you can get lower than "a" we can stop here.

Algorithm Approach 1

  Have two counters that start from the start and end of the string
  while left < right:
    Check if left is 'a' - if it is skip
    Check if right is 'a' - if it is skip
    If left is not 'a' - convert to 'a'
      - save to palindrome_left if it is smaller
    If right is not 'a - convert to 'a'
      - save to palindrome_right if it is smaller

    If left breaks palindrome, calc palindrom right break - compare - and take the one that is smaller

  Edge cases:
    - 'a' - one char string - breaking a palindrome is impossible
    - 'aaaaaa' - you want to change the last character to 'b'

"""

class Solution:
  def breakPalindrome(self, palindrome: str) -> str:
    # Edge cases
    if len(palindrome) == 1:
      return ''

    check_all_a = True
    for char in palindrome:
      if char != 'a':
        check_all_a = False

    if check_all_a:
      return palindrome[:len(palindrome) - 1] + 'b'

    left = 0
    right = len(palindrome) - 1
    palindrome_right = ''
    palindrome_left = ''
    while left < right:
      if palindrome[left] != 'a':
        new_palindrome = palindrome[:left] + 'a' + palindrome[left+1:]
        if palindrome_left == '':
          palindrome_left = new_palindrome
        else:
          palindrome_left = new_palindrome if new_palindrome < palindrome_left else palindrome_left
      elif palindrome[left] == 'a':
        new_palindrome = palindrome[:left] + 'b' + palindrome[left+1:]
        if palindrome_left == '':
          palindrome_left = new_palindrome
        else:
          palindrome_left = new_palindrome if new_palindrome < palindrome_left else palindrome_left

      if palindrome[right] != 'a':
        new_palindrome = palindrome[:right] + 'a' + palindrome[right+1:]
        if palindrome_right == '':
          palindrome_right = new_palindrome
        else:
          palindrome_right = new_palindrome if new_palindrome < palindrome_right else palindrome_right
      elif palindrome[left] == 'a':
        new_palindrome =  palindrome[:right] + 'b' + palindrome[right+1:]
        if palindrome_right == '':
          palindrome_right = new_palindrome
        else:
          palindrome_right = new_palindrome if new_palindrome < palindrome_right else palindrome_right
      left += 1
      right -= 1

    if palindrome_right < palindrome_left:
      return palindrome_right
    elif palindrome_left < palindrome_right:
      return palindrome_left
    else:
      return ''


sol = Solution()
print(sol.breakPalindrome('abccba'))
print(sol.breakPalindrome('a'))
print(sol.breakPalindrome('aaaaaa'))
print(sol.breakPalindrome('aba'))
print(sol.breakPalindrome('bbb'))
