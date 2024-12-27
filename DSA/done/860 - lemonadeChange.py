# https://leetcode.com/problems/lemonade-change/

from typing import List 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for b in bills:
            if b == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif b == 20:
                if (ten >= 1 and five >= 1):
                    ten -= 1
                    five -= 1
                elif (five >= 3):
                    five -= 3
                else:
                    return False
            else:
                five += 1

        return True