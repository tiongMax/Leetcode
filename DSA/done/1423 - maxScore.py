# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxS = 0
        currS = 0
        for i in range(k):
            currS += cardPoints[i]
        maxS = currS

        end = len(cardPoints) - 1
        for i in range(k):
            currS = currS - cardPoints[k - 1 - i] + cardPoints[end]
            maxS = max(maxS, currS)
            end -= 1

        return maxS
