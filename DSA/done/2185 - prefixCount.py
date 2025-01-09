# https://leetcode.com/problems/counting-words-with-a-given-prefix/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.count += 1

    def search(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.search(pref)
            
