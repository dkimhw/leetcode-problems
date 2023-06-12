
from easy.find_kth_positive_num import Solution

class TestFindKthPositiveSum:
  def test_should_return_nine(self):
    # prepare
    sol = Solution()
    nums = [2,3,4,7,11]
    k = 5

    # call
    result = sol.findKthPositive(nums, k)

    # assert
    assert result == 9

  def test_should_return_two(self):
    # prepare
    sol = Solution()
    nums = [1,2,3,4]
    k = 2

    # call
    result = sol.findKthPositive(nums, k)

    # assert
    assert result == 6

  def test_should_return_fourteen(self):
    # prepare
    sol = Solution()
    nums = [5,6,7,8,9]
    k = 9

    # call
    result = sol.findKthPositive(nums, k)

    # assert
    assert result == 14
