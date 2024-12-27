# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1: Using variable to store critical points
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        # Initialize pointers
        left = head
        middle = head.next
        right = head.next.next

        first_crit_index = -1
        last_crit_index = -1
        min_dist = float('inf')
        length = 0

        while right:
            length += 1

            # Check if middle is a critical point
            if (middle.val < left.val and middle.val < right.val) or \
                (middle.val > left.val and middle.val > right.val):
                if first_crit_index == -1:
                    first_crit_index = length
                else:
                    min_dist = min(min_dist, length - last_crit_index)

                last_crit_index = length

            # Move the pointers forward
            left = middle
            middle = right
            right = right.next

        if first_crit_index == -1 or first_crit_index == last_crit_index:
            return [-1, -1]

        return [min_dist, last_crit_index - first_crit_index]

# Approach 2: Using list to store critical points
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left = middle = right = head
        for i in range(2):
            if not right:
                return [-1, -1]
            right = right.next

        middle = middle.next
        crit = []
        length = 0
        min_dist = float('inf')
        while right:
            if (middle.val < right.val and middle.val < left.val) or \
                (middle.val > right.val and middle.val > left.val):
                crit.append(length + 1)

            if len(crit) >= 2:
                min_dist = min(min_dist, crit[-1] - crit[-2])

            length += 1
            left, middle, right = left.next, middle.next, right.next

        return [min_dist, crit[-1] - crit[0]] if len(crit) >= 2 else [-1, -1]