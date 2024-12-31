# https://leetcode.com/problems/course-schedule-ii/

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        for s, d in prerequisites:
            adj[s].append(d)

        visited, cycle = set(), set()
        mst = []

        def dfs(c):
            if c in visited:
                return True
            if c in cycle:
                return False 

            cycle.add(c)
            for n in adj[c]:
                if not dfs(n):
                    return False
            cycle.pop()
            visited.add(c)
            mst.append(c)
            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c):
                    return []

        return mst
                     
