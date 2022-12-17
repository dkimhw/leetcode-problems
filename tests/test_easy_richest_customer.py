
from easy.richest_customer import Solution

class TestRichestCustomer:
  def test_dup1_should_be_true(self):
    # arrange
    accounts = [[1,2,3],[3,2,1]]
    sol = Solution()

    # call
    result = sol.maximumWealth(accounts)

    # assert
    assert result == 6
