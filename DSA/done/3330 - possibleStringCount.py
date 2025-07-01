# https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = i = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                res += 1
        return res 
        