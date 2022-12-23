"""
Algorithm

Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1l1 and l2l2l2. Since each digit is in the range of 0…90 \ldots 90…9, summing two digits may "overflow". For example 5+7=125 + 7 = 125+7=12. In this case, we set the current digit to 222 and bring over the carry=1carry = 1carry=1 to the next iteration. carrycarrycarry must be either 000 or 111 because the largest possible sum of two digits (including the carry) is 9+9+1=199 + 9 + 1 = 199+9+1=19.

The pseudocode is as following:

Initialize current node to dummy head of the returning list.
Initialize carry to 000.
Loop through lists l1l1l1 and l2l2l2 until you reach both ends and carry is 000.
Set xxx to node l1l1l1's value. If l1l1l1 has reached the end of l1l1l1, set to 000.
Set yyy to node l2l2l2's value. If l2l2l2 has reached the end of l2l2l2, set to 000.
Set sum=x+y+carrysum = x + y + carrysum=x+y+carry.
Update carry=sum/10carry = sum / 10carry=sum/10.
Create a new node with the digit value of (sum mod 10)(sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
Advance both l1l1l1 and l2l2l2.
Return dummy head's next node.
Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

Take extra caution of the following cases:

Test case	Explanation
l1=[0,1]l1=[0,1]l1=[0,1]
l2=[0,1,2]l2=[0,1,2]l2=[0,1,2]	When one list is longer than the other.
l1=[]l1=[]l1=[]
l2=[0,1]l2=[0,1]l2=[0,1]	When one list is null, which means an empty list.
l1=[9,9]l1=[9,9]l1=[9,9]
l2=[1]l2=[1]l2=[1]	The sum could have an extra carry of one at the end, which is easy to forget.

"""
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode(0)
    curr = dummyHead # we are looping on dummy so we don't have to traverse linkedlist multiple, multiple times
    carry = 0
    while l1 != None or l2 != None or carry != 0:
      l1Val = l1.val if l1 else 0
      l2Val = l2.val if l2 else 0
      columnSum = l1Val + l2Val + carry
      carry = columnSum // 10 # Review this line
      # newNode = ListNode(columnSum % 10) # Review this line
      if columnSum > 9:
        newNode = ListNode(columnSum - 10)
      else:
        newNode = ListNode(columnSum)

      curr.next = newNode
      curr = newNode
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
    return dummyHead.next
