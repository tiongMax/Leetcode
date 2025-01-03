# https://leetcode.com/problems/parallel-courses-iii/

from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        for pre, nex in relations:
            graph[nex].append(pre)

        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]

            time_taken = 0
            for n in graph[node]:
                time_taken = max(time_taken, dfs(n))
                
            visited[node] = time_taken + time[node - 1]
            return visited[node]

        res = 0
        for i in range(1, n + 1):
            res = max(res, dfs(i))

        return res