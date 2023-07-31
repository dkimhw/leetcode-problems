

from easy.is_iso_strings import Solution

class TestIsISOString:
  def test_should_return_true(self):
    # prep
    sol = Solution()
    s = "paper"
    t = "title"

    # call
    result = sol.isIsomorphic(s, t)

    # assert
    assert result == True

  def test_should_return_false(self):
    # prep
    sol = Solution()
    s = "foo"
    t = "bar"

    # call
    result = sol.isIsomorphic(s, t)

    # assert
    assert result == False

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    s = "egg"
    t = "add"

    # call
    result = sol.isIsomorphic(s, t)

    # assert
    assert result == True
