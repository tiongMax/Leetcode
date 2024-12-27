# https://leetcode.com/problems/sort-the-people/

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        for i in range(len(names)):
            hm[heights[i]] = names[i]

        k = list(hm.keys())
        k.sort(reverse=True)
        return [hm[i] for i in k]