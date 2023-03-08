
from medium.num_tilings import Solution

class TestNumTilings:
  def test_should_return_5(self):
    # arrange
    sol = Solution()
    n = 3

    # execute
    result = sol.numTilings(n)

    # assert
    assert result == 5

  def test_should_return_1(self):
    # arrange
    sol = Solution()
    n = 1

    # execute
    result = sol.numTilings(n)

    # assert
    assert result == 1
