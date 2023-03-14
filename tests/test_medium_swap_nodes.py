
from medium.swap_nodes import Solution
from medium.swap_nodes import ListNode

class TestSwapNodes:
  def test_should_return_reverse(self):
    # arrange
    l4 = ListNode(4)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)
    sol = Solution()

    # Call function
    a = sol.swapPairs(l1)
    result = [a.val, a.next.val, a.next.next.val, a.next.next.next.val]

    assert  result == [2, 1, 4, 3]
