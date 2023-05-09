
from medium.subarrays_div_by_k import Solution

class TestSubArraysDivByK:
  def test_should_return_four(self):
    # prepare
    sol = Solution()
    nums = [1, 1, 1, 1]
    k = 2

    # call
    result = sol.subarraysDivByK(nums, k)

    assert result == 4


  def test_should_return_seven(self):
    # prepare
    sol = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5

    # call
    result = sol.subarraysDivByK(nums, k)

    assert result == 7
