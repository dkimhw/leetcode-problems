
from easy.check_almost_eq import Solution

class TestCheckAlmostEq:
  def test_should_return_false1(self):
    # prepare
    sol = Solution()
    word1 = "aaaa"
    word2 = "bccb"

    # call
    result = sol.checkAlmostEquivalent(word1, word2)

    # assert
    assert result == False

  def test_should_return_false2(self):
    # prepare
    sol = Solution()
    word1 = "zzzyyy"
    word2 = "iiiiii"

    # call
    result = sol.checkAlmostEquivalent(word1, word2)

    # assert
    assert result == False

  def test_should_return_true(self):
    # prepare
    sol = Solution()
    word1 = "abcdeef"
    word2 = "abaaacc"

    # call
    result = sol.checkAlmostEquivalent(word1, word2)

    # assert
    assert result == True
