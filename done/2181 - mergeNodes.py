# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1: 3 pointers
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = slow = ListNode(0, head)
        fast = head.next

        while fast:
            tmp = fast.val
            while fast.next.val != 0:
                fast = fast.next
                tmp += fast.val
            fast.val = tmp
            slow.next = fast
            slow = slow.next
            fast = fast.next.next

        if slow.next.val == 0:
            slow.next = fast
        return dummy.next
    
# Approach 2: 2 pointers
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur.next:
            node = cur.next
            cur = cur.next
            while cur.next.val != 0:
                node.val += cur.next.val
                cur = cur.next

            cur = cur.next
            node.next = cur.next
        return head.next