
from easy.first_recurring_char import Solution

class TestFirstRecurringChar:
  def test_should_return_true_example1(self):
    # arrange
    sol = Solution()
    nums = [2,5,1,2,3,5,1,2,4]

    # call
    result = sol.first_recurring_char(nums)

    # assert
    assert result == 2

  def test_should_return_true_example2(self):
    # arrange
    sol = Solution()
    nums = [2,1,1,2,3,5,1,2,4]

    # call
    result = sol.first_recurring_char(nums)

    # assert
    assert result == 1

  def test_should_return_true_example3(self):
    # arrange
    sol = Solution()
    nums = [2,3,4,5]

    # call
    result = sol.first_recurring_char(nums)

    # assert
    assert result == None
