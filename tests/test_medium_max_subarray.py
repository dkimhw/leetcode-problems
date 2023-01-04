from medium.max_subarray import Solution

class TestMaxSubArray:
  def test_should_return_true1(self):
    # define
    sol = Solution()
    nums = [-2, 10, -2, -2, 10]

    # call
    result = sol.maxSubArray(nums)

    # assert
    assert result == 16

  def test_should_return_true2(self):
    # define
    sol = Solution()
    nums = [-1,-1,-2,-2]

    # call
    result = sol.maxSubArray(nums)

    # assert
    assert result == -1

  def test_should_return_true3(self):
    # define
    sol = Solution()
    nums = [-1, 0]

    # call
    result = sol.maxSubArray(nums)

    # assert
    assert result == 0

  def test_should_return_true4(self):
    # define
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    # call
    result = sol.maxSubArray(nums)

    # assert
    assert result == 6

  def test_should_return_true5(self):
    # define
    sol = Solution()
    nums = [1,-2,0]

    # call
    result = sol.maxSubArray(nums)

    # assert
    assert result == 1
