# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        palin = set()
        for c in s:
            right[c] -= 1
            for l in left:
                if right[l] > 0:
                    palin.add((l, c))
            left.add(c)
        return len(palin)
                