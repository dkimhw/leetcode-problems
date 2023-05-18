
from medium.min_rounds import Solution

class TestMinRounds:
  def test_should_return_four(self):
    # arrange
    sol = Solution()
    tasks = [2,2,3,3,2,4,4,4,4,4]

    # call
    result = sol.minimumRounds(tasks)

    # assert
    assert result == 4

  def test_should_return_minus_one(self):
    # arrange
    sol = Solution()
    tasks = [2,2,3]

    # call
    result = sol.minimumRounds(tasks)

    # assert
    assert result == -1

  def test_should_return_two(self):
    # arrange
    sol = Solution()
    tasks = [7,7,7,7,7,7]

    # call
    result = sol.minimumRounds(tasks)

    # assert
    assert result == 2
