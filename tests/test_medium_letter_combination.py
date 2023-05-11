
from medium.letter_combination import Solution

class TestLetterCombination:
  def test_should_return_true1(self):
    # prepare
    sol = Solution()
    digits = '23'

    # call
    results = sol.letterCombinations(digits)

    # assert
    assert results == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

  def test_should_return_true2(self):
    # prepare
    sol = Solution()
    digits = ''

    # call
    results = sol.letterCombinations(digits)

    # assert
    assert results == []

  def test_should_return_true3(self):
    # prepare
    sol = Solution()
    digits = '2'

    # call
    results = sol.letterCombinations(digits)

    # assert
    assert results == ["a","b","c"]
