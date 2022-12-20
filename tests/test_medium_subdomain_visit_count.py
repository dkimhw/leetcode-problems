
from medium.subdomain_visit_count import Solution

class TestSubdomainVisitCount:
  def test_should_assert_true1(self):
    # arrange
    cpdomains = ["9001 discuss.leetcode.com"]
    sol = Solution()

    # call
    output = sol.subdomainVisits(cpdomains)

    # assert
    result = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]

    assert output == result

  def test_should_assert_true2(self):
    # arrange
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    sol = Solution()

    # call
    output = sol.subdomainVisits(cpdomains)

    # assert
    result = ["900 google.mail.com","901 mail.com","951 com","50 yahoo.com", "1 intel.mail.com","5 wiki.org", "5 org"]

    assert output == result
