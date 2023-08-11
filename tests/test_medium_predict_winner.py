
from medium.predict_winner import Solution

class TestPredictWinner:
  def test_should_return_true(self):
    # prep
    nums = [1,5,2]
    sol = Solution()

    # call
    result = sol.predictTheWinner(nums)

    # assert
    assert False == result

  def test_should_return_false(self):
    # prep
    nums = [1,5,233,7]
    sol = Solution()

    # call
    result = sol.predictTheWinner(nums)

    # assert
    assert True == result
