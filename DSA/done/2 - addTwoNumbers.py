# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = res = ListNode()
        while l1 or l2 or carry:
            left = l1.val if l1 else 0
            right = l2.val if l2 else 0

            sum = left + right + carry
            carry = 1 if sum > 9 else 0
            sum %= 10

            dummy.next = ListNode(sum)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return res.next


        