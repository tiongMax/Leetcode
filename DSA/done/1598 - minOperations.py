# https://leetcode.com/problems/crawler-log-folder/

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        lvl = 0
        for l in logs:
            if l == "../":
                if lvl > 0:
                    lvl -= 1
                else:
                    lvl = 0
            elif l == "./":
                continue
            else:
                lvl += 1

        return lvl
            