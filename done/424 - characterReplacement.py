# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = maxl = maxf = 0
        hm = [0] * 26
        while r < len(s):
            hm[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, hm[ord(s[r]) - ord('A')])
            if (r - l + 1) - maxf > k:
                hm[ord(s[l]) - ord('A')] -= 1
                l += 1
            if (r - l + 1) - maxf <= k:
                maxl = max(maxl, r - l + 1)
            r += 1

        return maxl