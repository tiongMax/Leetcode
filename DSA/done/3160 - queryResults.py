# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        ball_to_color, color_to_ball = {}, {}
        for b, c in queries:
            if b in ball_to_color:
                prev_color = ball_to_color[b]
                color_to_ball[prev_color] -= 1
                if color_to_ball[prev_color] == 0:
                    del color_to_ball[prev_color]
            
            ball_to_color[b] = c
            color_to_ball[c] = color_to_ball.get(c, 0) + 1
            res.append(len(color_to_ball))
        return res