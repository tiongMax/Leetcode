from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for s, d in prerequisites:
            adj[s].append(d)

        visited = set()
        cur_path = set()

        def dfs(c):
            if c in visited:
                return True

            if c in cur_path:
                return False

            cur_path.add(c)
            for n in adj[c]:
                if not dfs(n):
                    return False
            cur_path.remove(c)
            # If the question wants the topo order, this can be changed to stack 
            # or list.
            visited.add(c)
            return True

        for i in range(numCourses):
            if i not in visited: # Can be omitted but will be slightly slower.
                if not dfs(i):
                    return False
        return True
