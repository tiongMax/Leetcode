# https://leetcode.com/problems/split-linked-list-in-parts/

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the total number of nodes in the list
        total_nodes = 0
        current = head
        while current:
            total_nodes += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = total_nodes // k  # Base size of each part
        extra_nodes = total_nodes % k  # Number of parts that will get an extra node
        
        # Step 3: Split the list
        result = []
        current = head
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if extra_nodes > 0 else 0)  # Add extra node if needed
            extra_nodes -= 1
            # Move `current` to the end of this part
            for j in range(part_length - 1):
                if current:
                    current = current.next
            # Break the current part from the next part
            if current:
                next_part = current.next
                current.next = None  # Cut off this part
                current = next_part
            result.append(part_head)
        
        return result
