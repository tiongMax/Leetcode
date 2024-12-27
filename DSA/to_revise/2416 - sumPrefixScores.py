# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

from typing import List

# Definition for PrefixNode
class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

# Definition for PrefixTree
class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, w):
        cur = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = PrefixNode()
            cur = cur.children[i]
            cur.count += 1

    def get_score(self, w):
        cur = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            cur = cur.children[i]
            score += cur.count
        return score

# Solution class
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_tree = PrefixTree()
        
        # Insert all words into the prefix tree
        for w in words:
            prefix_tree.insert(w)

        # Calculate score for each word
        for w in words:
            res.append(prefix_tree.get_score(w))
        
        return res
