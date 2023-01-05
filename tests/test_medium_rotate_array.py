from medium.rotate_array import Solution

class TestRotateArray:
  def test_should_return_true_example1(self):
    # arrange
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3

    # call
    sol.rotate(nums, k)

    # assert
    assert nums == [5,6,7,1,2,3,4]

  def test_should_return_true_example2(self):
    # arrange
    sol = Solution()
    nums = [-1,-100,3,99]
    k = 2

    # call
    sol.rotate(nums, k)

    # assert
    assert nums == [3,99,-1,-100]
