# https://leetcode.com/problems/alice-and-bob-playing-flower-game

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2
    
# class Solution:
#     def flowerGame(self, n: int, m: int) -> int:
#         return ceil(n / 2) * floor(m / 2) + floor(n / 2) * ceil(n / 2)