# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 1. Build the graph
        graph = defaultdict(list)
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))
            
        # 2. Initialize BFS tools
        queue = deque([1])
        visited = set([1])
        min_score = float('inf')
        
        # 3. Traverse the component
        while queue:
            curr = queue.popleft()
            
            for neighbor, distance in graph[curr]:
                # Update the minimum score seen so far
                min_score = min(min_score, distance)
                
                # If we haven't been to this city, explore it
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score