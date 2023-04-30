
from medium.subarrays_div_by_k import Solution

class TestSubArraysDivByK:
  def test_should_return_2(self):
    # prepare
    sol = Solution()
    nums = [1, 1, 1, 1]
    k = 3

    # call
    result = sol.subarraysDivByK(nums, k)

    assert result == 2


  def test_should_return_seven(self):
    # prepare
    sol = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5

    # call
    result = sol.subarraysDivByK(nums, k)

    assert result == 7
