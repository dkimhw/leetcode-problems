
from easy.power_of_two import Solution

class TestPowerOfTwo:
  def test_should_return_true1(self):
    # arrange
    n = 16
    sol = Solution()

    # call
    result = sol.isPowerOfTwo(n)

    # assert
    assert result == True

  def test_should_return_true2(self):
    # arrange
    n = 1
    sol = Solution()

    # call
    result = sol.isPowerOfTwo(n)

    # assert
    assert result == True

  def test_should_return_false1(self):
    # arrange
    n = 3
    sol = Solution()

    # call
    result = sol.isPowerOfTwo(n)

    # assert
    assert result == False

  def test_should_return_false2(self):
    # arrange
    n = -16
    sol = Solution()

    # call
    result = sol.isPowerOfTwo(n)

    # assert
    assert result == False
