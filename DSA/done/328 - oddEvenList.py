# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 'odd' will track the end of the odd-indexed list
        # 'even' will track the end of the even-indexed list
        odd = head
        even = head.next
        # We need to save the start of the even list to connect it later
        even_head = even
        
        while even and even.next:
            # Connect current odd node to the next odd node
            odd.next = even.next
            odd = odd.next
            
            # Connect current even node to the next even node
            even.next = odd.next
            even = even.next
            
        # Join the odd list with the head of the even list
        odd.next = even_head
        
        return head