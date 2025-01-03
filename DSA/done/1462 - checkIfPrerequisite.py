# https://leetcode.com/problems/course-schedule-iv/submissions/1297670987/

from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]

            prereq = set()
            for n in graph[node]:
                prereq.add(n)
                prereq.update(dfs(n))

            visited[node] = prereq
            return prereq

        for c in range(numCourses):
            if c not in visited:
                dfs(c)

        res = []
        for s, d in queries:
            res.append(s in visited[d])

        return res
                