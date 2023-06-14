from easy.shuffle_array import Solution

class TestShuffleArray:
  def test_should_return_true1(self):
    # prep
    sol = Solution()
    nums = [2,5,1,3,4,7]
    n = 3

    # call
    result = sol.shuffle(nums, n)

    # assert
    assert result == [2,3,5,4,1,7]

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    nums = [1,2,3,4,4,3,2,1]
    n = 4

    # call
    result = sol.shuffle(nums, n)

    # assert
    assert result == [1,4,2,3,3,2,4,1]
