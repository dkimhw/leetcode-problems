
from easy.avg_salary import Solution

class TestAvgSalary:
  def test_should_return_2500(self):
    # prep
    sol = Solution()
    salary = [4000,3000,1000,2000]

    # call
    result = sol.average(salary)

    # assert
    assert result == 2500.0

  def test_should_return_2000(self):
    # prep
    sol = Solution()
    salary = [1000,2000,3000]

    # call
    result = sol.average(salary)

    # assert
    assert result == 2000.0
