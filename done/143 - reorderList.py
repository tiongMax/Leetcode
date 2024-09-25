# https://leetcode.com/problems/reorder-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid, end = head, head.next
        while end and end.next:
            mid = mid.next
            end = end.next.next

        l_half = mid.next
        mid.next = second = None
        while l_half:
            temp = l_half.next
            l_half.next = second
            second = l_half
            l_half = temp

        left, right = head, second
        while right:
            tmp1, tmp2 = left.next, right.next
            right.next = tmp1
            left.next = right
            left, right = tmp1, tmp2

