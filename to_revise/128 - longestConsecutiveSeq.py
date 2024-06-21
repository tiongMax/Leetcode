# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

# Approach 1: Union find
class UnionFind:
    def __init__(self, nums):
        self.par = {}
        self.rank = {}
        self.size = {}
        for i in nums:
            self.par[i] = i
            self.rank[i] = 1
            self.size[i] = 1

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
            self.size[p1] += self.size[p2]
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
            self.size[p2] += self.size[p1]
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = set(nums)
        edges = []
        for n in nums:
            if n + 1 in nums:
                edges.append([n, n + 1])

        uf = UnionFind(nums)
        for n1, n2 in edges:
            uf.union(n1, n2)

        return max(uf.size.values())
    
# Approach 2: Hash map
