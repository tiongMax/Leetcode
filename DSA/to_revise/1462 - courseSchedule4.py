# https://leetcode.com/problems/course-schedule-iv/submissions/1297670987/

from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]],
                                 queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False] * len(queries)

        adj = {i : [] for i in range(numCourses)}
        for s, d in prerequisites:
            adj[s].append(d)

        visited = set()
        prereq = defaultdict(set)

        def dfs(s):
            if s in visited:
                return prereq[s]

            for d in adj[s]:
                # Store the direct and indirect prereq in hashmap
                prereq[s].add(d)
                prereq[s].update(dfs(d))
            
            visited.add(s)
            return prereq[s]
        
        for s in adj.keys():
            if s not in visited:
                dfs(s)

        res = []
        for s, d in queries:
            res.append(d in prereq[s])

        return res


