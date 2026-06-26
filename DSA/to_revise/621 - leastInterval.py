# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count the frequencies of each task
        counter = Counter(tasks)
        
        # 2. Python's heapq is a min-heap. 
        # We use negative values to simulate a max-heap based on task frequency.
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)
        
        # 3. Queue to track tasks on cooldown: stores pairs of [remaining_count, available_time]
        cooldown_queue = deque()
        time = 0
        
        # 4. Process until both the heap and the cooldown queue are empty
        while max_heap or cooldown_queue:
            time += 1
            
            # If we have available tasks to run, pop the most frequent one
            if max_heap:
                # Add 1 to move closer to 0 (since it's a negative number)
                remaining = heapq.heappop(max_heap) + 1
                
                # If the task still needs to be run, put it in the cooldown queue
                if remaining != 0:
                    cooldown_queue.append([remaining, time + n])
                    
            # Check if the task at the front of the queue has finished its cooldown
            if cooldown_queue and cooldown_queue[0][1] == time:
                # Push it back into the max heap to be scheduled
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
                
        return time