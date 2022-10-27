
"""

Input: `head` - head node of a linked list
Output: boolean
  - True if it is a palindrome or false otherwise

Example:

sol.isPalindrome()

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
    return None


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)
traverse_list_nodes(head1)

# sol = Solution()
# print(sol.isPalindrome())
