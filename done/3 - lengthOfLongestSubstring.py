# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res = 0
        hm = set()
        for r in range(len(s)):
            while s[r] in hm:
                hm.remove(s[l])
                l += 1
            hm.add(s[r])
            res = max(res, r - l + 1)

        return res