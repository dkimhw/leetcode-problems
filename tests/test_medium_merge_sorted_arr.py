
from medium.merge_sorted_arr import Solution

class TestMergeSortedArr:
  def test_merge_sorted_arr1(self):
    # arrange
    sol = Solution()
    arr1 = [1, 2, 3]
    arr2 = [1, 4, 5, 6]

    # call
    result = sol.merge_sorted_array(arr1, arr2)

    # assert
    assert result == [1, 1, 2, 3, 4, 5, 6]
