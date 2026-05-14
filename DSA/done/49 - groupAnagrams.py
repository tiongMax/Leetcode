# https://leetcode.com/problems/group-anagrams/

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            conv = tuple(cnt)
            if conv in hm:
                hm[conv].append(s)
            else:
                hm[conv] = [s]

        return list(hm.values())