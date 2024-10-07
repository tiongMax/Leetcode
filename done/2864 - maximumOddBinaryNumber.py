# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt1 = 0
        for c in s:
            if c == "1":
                cnt1 += 1

        if cnt1 == 1:
            return "0" * (len(s) - 1) + "1"
        elif cnt1 > 1:
            return "1" * (cnt1 - 1) + "0" * (len(s) - cnt1) + "1"
        else:
            return s