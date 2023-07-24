
from easy.merge_alt import Solution

class TestMergeAlt:
  def test_should_return_true(self):
    # prep
    sol = Solution()
    str1 = "abc"
    str2 = "pqr"

    # call
    result = sol.mergeAlternately(str1, str2)

    # assert
    assert result == 'apbqcr'

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    str1 = "ab"
    str2 = "pqrs"

    # call
    result = sol.mergeAlternately(str1, str2)

    # assert
    assert result == 'apbqrs'
