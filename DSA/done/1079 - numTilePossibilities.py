# https://leetcode.com/problems/letter-tile-possibilities/

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        letter_cnt = Counter(tiles)
        
        def backtrack() -> int:
            total = 0
            for c in letter_cnt:
                if letter_cnt[c] > 0:
                    letter_cnt[c] -= 1
                    total += 1  

                    total += backtrack()

                    letter_cnt[c] += 1
            return total

        return backtrack()
