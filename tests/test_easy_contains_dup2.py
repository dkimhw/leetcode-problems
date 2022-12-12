
from easy.contains_dup2 import Solution

class TestContainsDup2:
  def test_dup1_should_be_true(self):
    # arrange
    nums = [1,2,3,1]
    k = 3
    sol = Solution()

    # call
    result = sol.containsNearbyDuplicate(nums, k)

    # assert
    assert result == True

  def test_dup2_should_be_true(self):
    # arrange
    nums = [1,0,1,1]
    k = 1
    sol = Solution()

    # call
    result = sol.containsNearbyDuplicate(nums, k)

    # assert
    assert result == True

  def test_dup3_should_be_false(self):
    # arrange
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()

    # call
    result = sol.containsNearbyDuplicate(nums, k)

    # assert
    assert result == False
