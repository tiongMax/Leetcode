# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        m, n = len(v1), len(v2)

        for i in range(max(n, m)):
            c1 = int(v1[i]) if i < m else 0
            c2 = int(v2[i]) if i < n else 0

            if c1 < c2:
                return -1
            elif c2 < c1:
                return 1

        return 0