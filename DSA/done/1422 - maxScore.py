# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        total_zeroes = s.count('0')
        cur_zero = ans = 0
        for i in range(1, len(s)):
            if s[i - 1] == '0':
                cur_zero += 1
                total_zeroes -= 1
            ans = max(ans, cur_zero + len(s) - total_zeroes - i)
        return ans