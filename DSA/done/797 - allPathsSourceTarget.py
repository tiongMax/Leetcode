from collections import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        curPath = []
        visited = set()

        def dfs(node):
            if node == len(graph) - 1:
                res.append(curPath.copy())
                return
            elif node in visited: # To avoid loop
                return

            visited.add(node)
            for neighbor in graph[node]:
                curPath.append(neighbor)
                dfs(neighbor)
                curPath.pop()
            visited.remove(node) # So that other path that can revisit this node

        curPath.append(0)
        dfs(0)
        return res