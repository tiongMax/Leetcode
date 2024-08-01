# https://leetcode.com/problems/number-of-senior-citizens/

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for s in details:
            if int(s[11:13]) > 60:
                res += 1

        return res