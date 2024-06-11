from collections import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        minHeap = []

        for i, l in enumerate(lists):
            if l:
                # If l.val is the same, python will break tie based on the 
                # next argument, so we need to add another int to facilitate this.
                heapq.heappush(minHeap, (l.val, i, l))
                # We only push the first element of all the linked lists to 
                # maintain the small size of the heap. 

        dummy = res = ListNode()

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            dummy.next = node
            dummy = dummy.next
            # If current node has next, we push it to the heap.
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return res.next
