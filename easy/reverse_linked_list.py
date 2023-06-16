
"""
Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/


Problem
-------------------
Input: pointer (i.e. head of a singly linked list)
Output: pointer (i.e. head of a reversed singly linked list)

Examples
-------------------

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

1 -> add to head [1]
2 -> add to head [2, 1]
3 -> add to head [3, 2, 1]


Algorithm
-------------------
1. Loop through the linked list
2. As you loop maintain another linked list
  - add to head each node you are looping through
3. Return new linked list



"""

from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = head
    new_head = None

    while curr_node:
      new_node = ListNode(curr_node.val)
      if new_head == None:
        new_head = new_node
      else:
        new_node.next = new_head
        new_head = new_node
      curr_node = curr_node.next

    return new_head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
result = sol.reverseList(head)

print(result.val)
print(result.next.val)
