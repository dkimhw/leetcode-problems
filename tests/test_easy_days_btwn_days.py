
from easy.days_btwn_dates import Solution

class TestDaysBtwnDates:
  def test_should_return_15(self):
    # assert
    sol = Solution()
    date1 = "2020-01-15"
    date2 = "2019-12-31"

    # call
    result = sol.daysBetweenDates(date1, date2)

    # assert
    assert 15 == result
