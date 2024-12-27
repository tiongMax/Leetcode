# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hm = [-1, -1, -1]  # Initialize with -1 to handle first occurrences
        l = count = 0
        for r in range(len(s)):
            hm[ord(s[r]) - ord('a')] = r
            if min(hm) >= 0:
                count += min(hm) + 1
        return count