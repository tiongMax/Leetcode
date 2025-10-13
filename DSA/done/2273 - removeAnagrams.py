# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def getFreq(word):
            res = [0] * 26
            for c in word:
                res[ord(c) - ord('a')] += 1
            return res

        prev_anag = getFreq(words[0])
        stack = [words[0]]
        for i in range(1, len(words)):
            if getFreq(words[i]) != prev_anag:
                stack.append(words[i])
                prev_anag = getFreq(words[i])
        
        return stack
