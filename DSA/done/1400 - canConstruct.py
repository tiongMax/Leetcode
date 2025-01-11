# https://leetcode.com/problems/construct-k-palindrome-strings/

from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
            
        hm = Counter(s)
        odd = 0
        for v in hm.values():
            if v % 2 == 1:
                odd += 1
            if odd > k:
                return False
        return True