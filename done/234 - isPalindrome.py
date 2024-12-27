# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next

        r = None
        while s:
            tmp = s.next
            s.next = r
            r = s
            s = tmp

        l = head
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            
        return True
            


