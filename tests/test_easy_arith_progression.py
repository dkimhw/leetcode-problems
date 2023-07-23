
from easy.arith_progression import Solution

class TestArithProgression:
  def test_should_return_true(self):
    # prep
    sol = Solution()
    nums = [0,0,0,0]

    # call
    result = sol.canMakeArithmeticProgression(nums)

    # assert
    assert True == result

  def test_should_return_false(self):
    # prep
    sol = Solution()
    nums = [1, 2, 3, 2, 5]

    # call
    result = sol.canMakeArithmeticProgression(nums)

    # assert
    assert False == result

  def test_should_return_true2(self):
    # prep
    sol = Solution()
    nums = [3,5,1]

    # call
    result = sol.canMakeArithmeticProgression(nums)

    # assert
    assert True == result
