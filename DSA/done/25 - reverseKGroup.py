# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Own
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create dummy node and slow fast pointers
        dummy = connect = ListNode()
        dummy.next = head
        fast = dummy.next 
        i = k

        while fast:
            # Move k times forward from head while head is not null
            while fast and i > 0:
                fast = fast.next
                i -= 1

            if i > 0 :
                break
            i = k - 1

            # Reverse dummy.next and update pointer
            slow = connect.next
            reverse = fast
            while slow != fast:
                temp = slow.next
                slow.next = reverse
                reverse = slow
                slow = temp
            
            connect.next = reverse
            
            # Proceed to the next iter
            while i >= 0:
                connect = connect.next
                i -= 1
            
            i = k

        return dummy.next

# Neetcode's
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
