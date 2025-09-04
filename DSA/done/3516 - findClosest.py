# https://leetcode.com/problems/find-closest-person

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff_x, diff_y = abs(x - z), abs(y - z)
        if diff_x < diff_y:
            return 1
        elif diff_x > diff_y:
            return 2
        return 0