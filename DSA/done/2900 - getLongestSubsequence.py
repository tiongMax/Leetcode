# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        need = groups[0]
        for i in range(len(words)):
            if need == groups[i]:
                res.append(words[i])
                need ^= 1
        return res