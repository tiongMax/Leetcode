# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = True
        while time >= n - 1:
            time -= n - 1
            direction = not direction

        return 1 + time if direction else n - time