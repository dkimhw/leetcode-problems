
from medium.house_robber import Solution

class TestHouseRobber:
  def test_should_return_4(self):
    # prep
    sol = Solution()
    nums = [1,2,3,1]

    # call
    result = sol.rob(nums)

    # assert
    assert result == 4

  def test_should_return_12(self):
    # prep
    sol = Solution()
    nums = [2,7,9,3,1]

    # call
    result = sol.rob(nums)

    # assert
    assert result == 12
