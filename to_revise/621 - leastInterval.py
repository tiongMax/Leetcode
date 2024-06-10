class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            # If maxHeap is empty, it means that the CPU is currently idle.
            # So we just have to swift the time to the moment when the first
            # task from the queue can be processed again.
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                # If the amount of that task is not zero, we just insert it to the queue,
                # with updated amount and time.
                if cnt:
                    q.append([cnt, time + n])
            
            # If the current time is the same as the time for the first element from the
            # queue to be processed again, we push it into the heap again.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time