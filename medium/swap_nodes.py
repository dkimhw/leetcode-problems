"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/
Input: List of list nodes
Output: list node

Examaple:

Given a linked list, swap every two adjacent nodes and return its head.
 *e.g.*  for a list 1-> 2 -> 3 -> 4, one should return the head of list as 2 -> 1 -> 4 -> 3.

Algorithm:
1. Swap the head and head.next
2. Recursively call the next node and swap. For each sublist - attach the returned sublist with head

"""

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def swap(node):
      # swap node and node.next
      if node and node.next:
        next_node = None
        if node.next.next:
          next_node = node.next.next

        tmp_node = node
        node = node.next
        tmp_node.next = None
        node.next = tmp_node

        # print(node.val)
        # print(node.next.val)
        # print(next_node.val)

        if next_node != None:
          next_node_to_link = swap(next_node)
          # print("next_node_to_link", next_node_to_link)
          node.next.next = next_node_to_link
      return node

    return swap(head)

l4 = ListNode(4)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
print("l1:", l1.val, " ", l2.val)
sol = Solution()
a = sol.swapPairs(l1)
print(a.val, a.next.val, a.next.next.val, a.next.next.next.val)
