from medium.break_palindrome import Solution

# print(sol.breakPalindrome('abccba'))
# print(sol.breakPalindrome('a'))
# print(sol.breakPalindrome('aaaaaa'))
# print(sol.breakPalindrome('aba'))
# print(sol.breakPalindrome('bbb'))
class TestBreakPalindrome:
  def test_should_return_aaccba(self):
    # arrange
    sol = Solution()
    palindrome = 'abccba'

    # call
    result = sol.breakPalindrome(palindrome)

    # assert
    assert result == 'aaccba'

  def test_should_return_empty_string(self):
    # arrange
    sol = Solution()
    palindrome = 'a'

    # call
    result = sol.breakPalindrome(palindrome)

    # assert
    assert result == ''

  def test_should_return_abb(self):
    # arrange
    sol = Solution()
    palindrome = 'bbb'

    # call
    result = sol.breakPalindrome(palindrome)

    # assert
    assert result == 'abb'

  def test_should_return_aaaaab(self):
    # arrange
    sol = Solution()
    palindrome = 'aaaaaa'

    # call
    result = sol.breakPalindrome(palindrome)

    # assert
    assert result == 'aaaaab'
