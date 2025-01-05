# https://leetcode.com/problems/shifting-letters-ii/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)
        for left, right, d in shifts:
            prefix_diff[right + 1] += 1 if d else -1
            prefix_diff[left] += -1 if d else 1

        diff = 0
        res = [ord(c) - ord('a') for c in s]
        for i in range(len(prefix_diff) - 1, -1, -1):
            diff += prefix_diff[i]
            res[i - 1] = (diff + res[i - 1] + 26) % 26

        print(s)
        s = [chr(ord('a') + n) for n in res]
        return "".join(s)
