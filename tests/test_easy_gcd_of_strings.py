
from easy.gcd_of_strings import Solution

class TestGcdOfStrings:
  def test_should_return_true1(self):
    # prep
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"

    # call
    result = sol.gcdOfStrings(str1, str2)

    # assert
    assert "ABC" == result

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"

    # call
    result = sol.gcdOfStrings(str1, str2)

    # assert
    assert "AB" == result

  def test_should_return_true3(self):
    # prep
    sol = Solution()
    str1 = "LEET"
    str2 = "CODE"

    # call
    result = sol.gcdOfStrings(str1, str2)

    # assert
    assert "" == result

  def test_should_return_true4(self):
    # prep
    sol = Solution()
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

    # call
    result = sol.gcdOfStrings(str1, str2)

    # assert
    assert "TAUXX" == result

  def test_should_return_true4(self):
    # prep
    sol = Solution()
    str1 = "ABABABAB"
    str2 = "ABAB"

    # call
    result = sol.gcdOfStrings(str1, str2)

    # assert
    assert "ABAB" == result
