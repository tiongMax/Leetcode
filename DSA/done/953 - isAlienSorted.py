# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {o: i for i, o in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if hm[w1[j]] > hm[w2[j]]:
                        return False
                    break
        
        return True 
