
"""

Input: string
Output: boolean
  - return true if the `s` can be palindrome after deleteing at most one character from it

Test Cases

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false


Brute Force:
- Start from first character
  - Delete char
  - Check if palindrome
  - Return true if palindrome
- To check if its a palindrome and checking n characters: O(n^2)


O(n) algorithm:
- Have a left, right idx
- while left < right
  - check s[left] === s[right]
  - if not equal:
    - We need to check if deleting the left or deleting the right will work
    - Both or only one of them might work
  - Note that since up to this point, it was a palindrome
    - we can just check palindrome for the remaining script deleting the left
    - or deleting the right
  - Call palindrome on both potential solutions


a b c a

left = 0
right = 3

left = 1
right = 2

not equal so delete right c and decrement right
- is it equal? yes and left = right - then end


"""

class Solution:
  def validPalindrome(self, s: str) -> bool:
    def is_palindrome(s: str, left: int, right: int) -> bool:
      while left < right:
        if s[left] != s[right]:
          return False
        left += 1
        right -= 1
      return True

    left = 0
    right = len(s) - 1

    while left < right:
      # Main logic for removing a character
      if s[left] != s[right]:
        delete_left = is_palindrome(s, left + 1, right)
        delete_right = is_palindrome(s, left, right - 1)
        if delete_left == False and delete_right == False:
          return False
        else:
          return True
      left += 1
      right -= 1
    return True


sol = Solution()
print(sol.validPalindrome("abca")) # True
print(sol.validPalindrome("abc")) # False
print(sol.validPalindrome("eeccccbebaeeabebccceea")) # false
print(sol.validPalindrome("ebcbbececabbacecbbcbe")) # true

"ebcbb cec abba cec bbcbe"
