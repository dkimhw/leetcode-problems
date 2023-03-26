

from easy.max_profit import Solution

class TestMaxProfit:
  def test_should_return_five(self):
    # prep
    sol = Solution()
    prices = [7,1,5,3,6,4]

    # call
    result = sol.maxProfit(prices)

    # assert
    assert result == 5

  def test_should_return_zero(self):
    # prep
    sol = Solution()
    prices = [7,6,4,3,1]

    # call
    result = sol.maxProfit(prices)

    # assert
    assert result == 0
