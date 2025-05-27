# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        reverse = None
        while trav:
            tmp = trav.next
            trav.next = reverse
            reverse = trav
            trav = tmp

        return reverse