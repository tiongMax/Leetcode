# https://leetcode.com/problems/sort-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 0 or 1 nodes are already sorted
        if not head or not head.next:
            return head

        # 1. Split the list into two halves using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # Crucial: Break the link to create two separate lists

        # 2. Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3. Merge the two sorted halves and return the result
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Attach the remaining nodes (if any)
        curr.next = list1 if list1 else list2
        
        return dummy.next
        