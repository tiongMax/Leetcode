# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for r in range(len(s) - 1, -1, -1):
            if s[r] == ' ' and res > 0:
                break
            if s[r] != ' ':
                res += 1

        return res