
from easy.degree_of_array import Solution

class TestDegreeOfArray:
  def test_should_return_6(self):
    # prep
    sol = Solution()
    nums = [1,2,2,3,1,4,2]

    # call
    results = sol.findShortestSubArray(nums)

    # assert
    assert results == 6

  def test_should_return_2(self):
    # prep
    sol = Solution()
    nums = [1,2,2,3,1]

    # call
    results = sol.findShortestSubArray(nums)

    # assert
    assert results == 2
