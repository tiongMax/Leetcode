# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drink = 0

        while full > 0:
            drink += full
            temp = empty + full
            full = temp // numExchange 
            empty = temp % numExchange

        return drink