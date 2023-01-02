
from easy.move_zeroes import Solution

class TestMoveZeroes:
  def test_should_return_sorted_arr(self):
    # arrange
    sol = Solution()
    arr = [0,1,0,3,12]

    # call
    sol.moveZeroes(arr)

    assert arr == [1,3,12,0,0]

  def test_should_return_sorted_arr2(self):
    # arrange
    sol = Solution()
    arr = [0]

    # call
    sol.moveZeroes(arr)

    assert arr == [0]
