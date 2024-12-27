# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hm = set(nums)

        dummy = ListNode(next=head)
        trav2 = dummy
        trav = dummy.next 
        while trav:
            if trav.val in hm:
                trav2.next = trav.next
            else:
                trav2 = trav
            trav = trav.next

        return dummy.next
