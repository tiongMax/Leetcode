# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n: int) -> int:
        return (4 * n * (n - 1) // 2) + 1