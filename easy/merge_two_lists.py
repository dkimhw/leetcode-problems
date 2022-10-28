
"""
Input: Two heads of linked lists
Output: One head of a merged linked list

Example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Algorithms:

Step 1: Start looping through list1 and list2
Step 2: Compare the curr_val1 and curr_val2
  - if curr_val1 <= curr_val2: append curr_val1 to results list via self.next
    - an move the index further for list1
  - if curr_val2 < curr_val1: append curr_val2 to results list via self.next
    - and move the index further for list2
Step 3: Return result head
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def appendList(self, list: Optional[ListNode], newVal):
      head = list
      while head:
        if head.next == None:
          head.next = ListNode(newVal)
          break
        head = head.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      result = None
      idx1 = list1
      idx2 = list2
      while idx1 or idx2:
        curr_val1 = idx1.val if idx1 else None
        curr_val2 = idx2.val if idx2 else None

        print(curr_val1)
        if curr_val2 is None or curr_val1 <= curr_val2:
          if result is None:
            result = idx1
          # else:
          #   self.appendList(result, curr_val1)

          idx1 = idx1.next
        elif curr_val1 is None or curr_val2 < curr_val1:
          if result is None:
            result = idx2
          # else:
          #   self.appendList(result, curr_val2)
          idx2 = idx2.next
      return result

sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

r = sol.mergeTwoLists(list1, list2)

# def traverse_list_nodes(head):
#   curr_node = head
#   while curr_node:
#     print(curr_node.val)
#     curr_node = curr_node.next

# traverse_list_nodes(r)
