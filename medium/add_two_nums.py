
"""
https://leetcode.com/problems/add-two-numbers/

Input: Two non-empty linked lists
  - each element: single digit
  - stored in reverse order
  - assume no leading zeros
Output: new linked list containing the sum of two linked list


Examples:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Looks like the hardest part of this will be to manage the carry over digits


General Algorithm:
- Loop over the two linked lists
- For each element, add them together
  - If the sum of the two results in a carry
  - create a new linked node
    - if `new_linked_nodes` - assign new linked node with val
    - if `carry` is true - add 1 in the next digit
      - keep track of a current_carry variable 0 or 1 depending on whether the carry exists

Looping a List Node:
- while current_node is not none
  - extract val
  - set current_node = this.next

Create a way to easily add to the tail of the ListNode
- Loop from start of linkedlist until we hit "None" (true condition)
- Then:
  - set the *current node* next value to the ListNode obj we want to append

Carry Logic
- 99
- 99
- 9 + 9 = 18 -> 8, carry 1
- 18 + 1 = 198
"""
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  # Append to tail of ListNode
  def appendToLinkedList(self, nodes: Optional[ListNode], new_node: ListNode):
    curr_node = nodes
    while True:
      if curr_node.next == None:
        curr_node.next = new_node
        return
      curr_node = nodes.next

  # Returns (carry: boolean, sum: integer)
  def addTwoDigits(self, digit1: ListNode, digit2: ListNode, carry: int):
    new_val = 0
    if digit1 is not None and digit2 is not None:
      new_val = digit1.val + digit2.val + carry
      print("addTwoDigits: ", new_val)
      if new_val > 9:
        return (True, new_val - 10)
      else:
        return (False, new_val)
    elif digit1 is not None:
      return (False, digit1.val + carry)
    else:
      return (False, digit2.val + carry)

  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    current_node_l1 = l1
    current_node_l2 = l2
    new_linked_nodes = None
    current_carry = 0
    while current_node_l1 != None or current_node_l2 != None:
      new_val = self.addTwoDigits(current_node_l1, current_node_l2, current_carry)
      print("l1:", current_node_l1.val)
      print("l2:", current_node_l2.val)
      print("new_val: ", new_val)
      if new_linked_nodes is None:
        new_linked_nodes = ListNode(new_val[1])
      else:
        self.appendToLinkedList(new_linked_nodes, ListNode(new_val[1], None))

      if new_val[0]:
        current_carry = 1
      else:
        current_carry = 0

      current_node_l1 = current_node_l1.next if current_node_l1 is not None else None
      current_node_l2 = current_node_l2.next if current_node_l2 is not None else None
    if current_carry == 1:
      self.appendToLinkedList(new_linked_nodes, ListNode(1, None))
    return new_linked_nodes

sol = Solution()
# a = ListNode(2)
# b = ListNode(4)
# c = ListNode(3)

# a.next = b
# b.next = c

# d = ListNode(5)
# e = ListNode(6)
# f = ListNode(4)

# d.next = e
# e.next = f

# sol = Solution()

# result = sol.addTwoNumbers(a, d)

# print(result.val)
# print(result.next.val)
# print(result.next.next.val)


a1 = ListNode(9)
a2 = ListNode(9)
a1.next = a2

b1 = ListNode(9)
b2 = ListNode(9)
b1.next = b2

result2 = sol.addTwoNumbers(a1, b1)

curr = result2
while  curr is not None:
  print(curr.val)
  curr = curr.next


# current_node_l1 = a1
# current_node_l2 = b1
# while current_node_l1 != None or current_node_l2 != None:
#   print("l1:", current_node_l1.val)
#   print("l2:", current_node_l2.val)
#   current_node_l1 = current_node_l1.next #if current_node_l1 is not None else None
#   current_node_l2 = current_node_l2.next #if current_node_l2 is not None else None


# print(result2.next.next.val)
# def appendToLinkedList(nodes: Optional[ListNode], new_node: ListNode):
#   curr_node = nodes
#   while curr_node is not None:
#     print(curr_node.val)
#     if curr_node.next == None:
#       curr_node.next = new_node
#       return
#     curr_node = nodes.next

# x = ListNode(5)
# y = ListNode(6)
# x.next = y
# appendToLinkedList(x, ListNode(8))

# blah = x
# while blah is not None:
#   print(blah.val)
#   blah = blah.next
