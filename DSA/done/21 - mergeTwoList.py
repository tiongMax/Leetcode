# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val <= list2.val:
                return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
            else:
                return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
            
# Iterative
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode() 

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  
                list1 = list1.next    
            else:
                current.next = list2  
                list2 = list2.next    
            current = current.next    

        current.next = list1 if list1 else list2
        return dummy.next  