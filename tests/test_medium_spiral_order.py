
from medium.spiral_order import Solution


class TestSpiralOrder:
  def test_should_return_true1(self):
    # prep
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    # call
    result = sol.spiralOrder(matrix)

    # assert
    assert result == [1,2,3,6,9,8,7,4,5]

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    # call
    result = sol.spiralOrder(matrix)

    # assert
    assert result == [1,2,3,4,8,12,11,10,9,5,6,7]
