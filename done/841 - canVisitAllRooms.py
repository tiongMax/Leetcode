from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        def dfs(node):
            visited[node] = True
            for k in rooms[node]:
                if not visited[k]:
                    dfs(k)

        dfs(0)
        return all(visited)