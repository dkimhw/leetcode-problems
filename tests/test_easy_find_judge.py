
from easy.find_judge import Solution


class TestFindJudge:
  def test_should_return_three (self):
    # prep
    sol = Solution()
    n = 3
    trust = [[1,3],[2,3]]

    # call
    result = sol.findJudge(n, trust)

    # assert
    assert result == 3

  def test_should_return_minus_one (self):
    # prep
    sol = Solution()
    n = 3
    trust = [[1,3],[2,3],[3,1]]

    # call
    result = sol.findJudge(n, trust)

    # assert
    assert result == -1

  def test_should_return_two (self):
    # prep
    sol = Solution()
    n = 2
    trust = [[1,2]]

    # call
    result = sol.findJudge(n, trust)

    # assert
    assert result == 2


  def test_should_return_ten (self):
    # prep
    sol = Solution()
    n = 30
    trust = [[20,25],[6,28],[21,28],[19,4],[17,20],[22,19],[20,7],[18,19],[23,26],[21,6],[15,30],[11,22],[24,14],[14,1],[1,28],[25,15],[13,20],[2,27],[26,12],[27,1],[30,14],[28,10],[29,11],[6,23],[30,16],[19,13],[7,22],[18,10],[21,15],[22,12],[23,9],[8,18],[11,15],[9,19],[24,21],[14,8],[12,8],[15,13],[2,18],[3,11],[1,15],[4,12],[28,1],[2,12],[5,1],[3,17],[6,14],[19,18],[7,15],[20,21],[18,5],[16,29],[21,8],[23,6],[9,20],[24,28],[14,19],[12,7],[15,10],[24,2],[4,11],[2,7],[5,10],[3,22],[30,2],[4,17],[19,27],[5,20],[16,20],[22,30],[18,22],[9,29],[14,26],[26,25],[24,9],[12,20],[27,20],[13,25],[28,23],[2,30],[26,3],[29,22],[27,10],[4,24],[28,13],[20,27],[16,11],[21,26],[17,10],[7,27],[22,17],[23,20],[21,4],[8,7],[22,11],[9,6],[14,29],[11,8],[14,7],[12,19],[1,18],[25,13],[15,6],[13,18],[2,25],[26,10],[3,4],[27,3],[30,12],[4,7],[28,4],[5,6],[16,2],[6,21],[30,22],[19,15],[7,16],[20,8],[18,8],[16,24],[8,14],[22,2],[23,11],[24,23],[12,10],[26,21],[3,13],[4,14],[28,3],[2,10],[5,15],[29,2],[3,19],[6,12],[4,20],[7,9],[21,22],[18,29],[8,27],[9,26],[14,17],[12,1],[15,20],[13,4],[26,28],[24,4],[25,1],[5,8],[29,27],[4,19],[19,29],[7,6],[16,22],[6,25],[19,3],[17,23],[18,20],[8,2],[9,3],[14,24],[24,11],[12,22],[27,22],[25,10],[28,17],[2,28],[26,1],[29,20],[5,27],[29,14],[16,13],[21,24],[19,8],[17,8],[7,21],[18,15],[23,22],[21,2],[8,9],[22,9],[23,12],[15,26],[11,10],[24,18],[14,5],[1,16],[13,16],[2,23],[3,6],[1,10],[4,1],[5,4],[16,4],[19,17],[17,1],[20,10],[18,6],[16,26],[9,13],[23,5],[8,22],[11,3],[9,23],[24,25],[12,4],[25,20],[15,9],[13,9],[26,19],[3,15],[27,26],[28,29],[2,8],[5,13],[3,21],[6,2],[7,11],[5,23],[20,17],[18,1],[16,17],[21,20],[23,2],[8,29],[14,23],[12,3],[25,29],[15,22],[13,2],[24,6],[27,19],[1,4],[13,28],[28,20],[26,4],[29,25],[27,9],[30,6],[4,29],[5,16],[20,24],[19,5],[7,30],[22,18],[20,6],[23,27],[21,7],[9,1],[14,30],[24,13],[12,16],[1,29],[25,8],[13,21],[2,26],[26,15],[29,18],[27,14],[28,9],[5,25],[29,12],[16,15],[6,22],[30,19],[19,10],[7,23],[20,13],[18,13],[23,16],[8,11],[9,10],[23,14],[8,17],[11,12],[14,11],[12,15],[1,22],[15,2],[13,14],[2,21],[3,8],[27,7],[2,15],[29,5],[16,6],[6,9],[30,26],[7,12],[18,4],[16,28],[17,25],[18,30],[23,7],[8,24],[9,21],[24,27],[14,18],[25,26],[15,11],[13,7],[11,27],[26,17],[4,10],[2,6],[5,11],[30,29],[5,21],[17,18],[22,25],[23,28],[9,30],[15,16],[26,24],[24,8],[12,27],[1,26],[25,5],[13,26],[28,22],[30,4],[7,2],[16,10],[6,29],[17,11],[22,16],[18,16],[21,5],[22,10],[9,7],[11,9],[14,6],[12,18],[1,19],[13,19],[2,24],[26,13],[3,5],[4,6],[28,11],[5,7],[29,10],[16,1],[30,17],[19,12],[17,12],[7,17],[20,15],[23,18],[8,13],[22,13],[23,8],[11,14],[9,18],[14,9],[15,12],[3,10],[1,14],[3,16],[6,15],[30,24],[19,21],[7,14],[20,22],[16,30],[22,4],[18,28],[23,1],[8,26],[11,7],[9,27],[24,29],[25,24],[15,21],[13,5],[1,7],[25,2],[2,4],[3,25],[4,18],[19,26],[5,19],[20,29],[16,21],[6,24],[21,16],[7,29],[8,1],[9,28],[14,27],[15,18],[11,18],[24,10],[12,21],[13,24],[28,16],[30,10],[4,25],[28,14],[16,12],[21,25],[17,9],[7,26],[20,2],[18,14],[9,5],[23,13],[24,17],[14,4],[1,17],[15,1],[13,17],[2,22],[26,11],[27,2],[1,11],[28,5],[29,8],[6,10],[30,23],[7,19],[20,9],[16,25],[21,12],[8,15],[23,10],[8,21],[15,14],[13,10],[26,18],[3,12],[5,14],[29,1],[6,13],[7,8],[20,16],[17,29],[22,26],[23,3],[9,25],[15,23],[13,3],[24,5],[12,24],[13,29],[28,27],[26,7],[3,27],[6,4],[30,1],[4,28],[16,23],[6,30],[19,2],[20,5],[8,3],[24,12],[14,3],[12,23],[1,30],[2,29],[26,14],[29,19],[27,15],[28,8],[5,26],[29,13],[16,14],[30,18],[19,11],[17,15],[20,12],[23,17],[8,10],[9,11],[23,15],[8,16],[11,13],[14,10],[12,14],[15,3],[2,20],[3,9],[27,4],[4,2],[2,14],[5,3],[29,6],[6,8],[30,21],[19,16],[7,13],[16,27],[21,10],[17,26],[23,4],[8,23],[24,26],[12,5],[15,8],[11,24],[26,16],[3,14],[1,2],[4,9],[28,30],[2,9],[3,20],[6,3],[30,28],[7,10],[20,18],[16,18],[21,19],[17,19],[22,24],[18,24],[25,28],[11,17],[26,27],[27,18],[1,27],[25,6],[28,21],[26,5],[3,29],[27,8],[4,30],[19,30]]

    # call
    result = sol.findJudge(n, trust)

    # assert
    assert result == 10
