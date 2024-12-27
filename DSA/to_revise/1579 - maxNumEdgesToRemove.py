# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

from typing import List

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        self.cnt = n
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]

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

        self.cnt -= 1
        return True  

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a, b = UnionFind(n), UnionFind(n)
        res = 0

        # Filling in the type 3 edges first is important. Consider two nodes 
        # connect by 3 different type of edges, filling the type 3 will result 
        # in a redundant of 2 edges while filling in any of the other will 
        # only result in 1.
        for t, s, d in edges:
            s -= 1
            d -= 1
            if t == 3:
                # When both of them fail, it means that there is a redundant
                # edge in both a set and b set. Since we are currently 
                # filling in type 3 edges, when 1 of the set has redundant
                # edge, the other will DEFINITELY have.
                if not a.union(s, d) or not b.union(s, d):
                    res += 1

        for t, s, d in edges:
            s -= 1
            d -= 1
            if t == 1:
                if not a.union(s, d):
                    res += 1
            elif t == 2:
                if not b.union(s, d):
                    res += 1

        return res if a.cnt == 1 and b.cnt == 1 else -1
