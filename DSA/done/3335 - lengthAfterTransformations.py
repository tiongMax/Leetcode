# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

from collections import deque

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        queue = deque([0] * 26)
        for c in s:
            queue[ord(c) - 97] += 1
        for _ in range(t):
            queue[0] += queue[25] 
            queue.appendleft(queue.pop())
        return sum(queue) % (10 ** 9 + 7)