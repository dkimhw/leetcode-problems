
"""
Problem
---------------

Input: pointer to head of a linked list (ListNode type)
Output: ListNode
  - middle node
  - if two middle nodes - return the second middle node

Examples
---------------

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Algorithm
---------------
1. Find the size of the linked list
  - Traverse until curr node is None
  - Keep a counter of each iteration
  - Return counter
2. If the size of the linked list is odd:
  - 5 / 2 = 2.5 - round down
  - return the 2nd node
3. If the size of the linked list is even:
  - 6 / 2 = 3
  - return the 3rd node

"""

from typing import Optional
import math

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def findLength(self, head: Optional[ListNode]) -> int:
    curr_node = head
    length = 0
    while curr_node:
      length += 1
      curr_node = curr_node.next

    return length

  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    linked_list_length = self.findLength(head)
    node_idx_to_return = linked_list_length / 2 if linked_list_length % 2 == 0 else math.floor(linked_list_length / 2)
    curr_counter = 0
    curr_node = head

    while curr_node:
      print(curr_node.val, node_idx_to_return)
      if curr_counter == node_idx_to_return:
        return curr_node
      curr_counter += 1
      curr_node = curr_node.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(sol.middleNode(head).val)
