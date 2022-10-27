
"""

Input: `head` - head node of a linked list
Output: boolean
  - True if it is a palindrome or false otherwise

Example:

1 - 2 - 2 - 1 # True
1 - 2 # False

Algorithm:

- Traverse through the linked list and append each val to a list data structure
- Compare the list to a reversed list of itself and return true if same

"""



# Definition for singly-linked list.
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def traverse_list_nodes(head):
  curr_node = head
  while curr_node:
    print(curr_node.val)
    curr_node = curr_node.next


class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    vals = []
    curr_node = head
    while curr_node:
      vals.append(curr_node.val)
      curr_node = curr_node.next
    vals_reverse = vals[:]
    vals_reverse.reverse()
    return vals == vals_reverse


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
traverse_list_nodes(head1)

sol = Solution()
print(sol.isPalindrome(head1)) # expect True


head2 = ListNode(1)
head2.next = ListNode(2)
sol = Solution()
print(sol.isPalindrome(head2)) # expect False
