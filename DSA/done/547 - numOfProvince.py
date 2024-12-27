# https://leetcode.com/problems/number-of-provinces/description/

from typing import List
from collections import defaultdict

# Approach 1: UnionFind
class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):  # No need to check isConnected[i][i] and only check upper triangle matrix
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        uniq_par = {uf.find(i) for i in range(n)}
        return len(uniq_par)

# Approach 2: DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        if not M:
            return 0
        
        n = len(M)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visit = [False] * n
        
        def dfs(u):
            for v in graph[u]:
                if visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                dfs(i)
        
        return count