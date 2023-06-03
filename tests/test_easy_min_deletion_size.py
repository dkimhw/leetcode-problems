
from easy.min_deletion_size import Solution


class TestMinDeletionSize:
  def test_should_return_3(self):
    # arrange
    sol = Solution()
    arr = ["zyx","wvu","tsr"]

    # call
    result = sol.minDeletionSize(arr)

    # assert
    assert result == 3

  def test_should_return_0(self):
    # arrange
    sol = Solution()
    arr = ["a","b"]

    # call
    result = sol.minDeletionSize(arr)

    # assert
    assert result == 0

  def test_should_return_1(self):
    # arrange
    sol = Solution()
    arr = ["cba","daf","ghi"]

    # call
    result = sol.minDeletionSize(arr)

    # assert
    assert result == 1
