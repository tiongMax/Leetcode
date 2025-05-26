# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

from collections import defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        hashmap = defaultdict(list)

        for u, v in edges:
            if u == v:
                return -1
            hashmap[u].append(v)

        visited = set()
        memo = {}
        def dfs(cur, target):
            if (cur, target) in memo:
                return memo[(cur, target)]

            result = 0
            for adj in hashmap[cur]:
                if adj in visited:
                    return float('inf')
                visited.add(adj)
                result = max(result, dfs(adj, target))
                visited.remove(adj)

            memo[(cur, target)] = result + 1 if colors[cur] == target else result
            return memo[(cur, target)]

        max_path_value = 0
        for i in range(len(colors)):
            max_path_value = max(max_path_value, dfs(i, colors[i]))

        return -1 if max_path_value == float('inf') else max_path_value