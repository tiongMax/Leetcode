# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List

# Approach 1: O(N)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pCount, sCount = [0] * 26, [0] * 26
        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1 
            sCount[ord(s[i]) - ord('a')] += 1 
        
        res = []
        matches = 0
        for i in range(26):
            if pCount[i] == sCount[i]:
                matches += 1
        
        l = 0
        for r in range(len(p), len(s)):
            if matches == 26:
                res.append(l)
            
            ind = ord(s[r]) - ord('a')
            sCount[ind] += 1 
            if sCount[ind] == pCount[ind]:
                matches += 1
            elif sCount[ind] == pCount[ind] + 1:
                matches -= 1

            ind = ord(s[l]) - ord('a')
            sCount[ind] -= 1 
            if sCount[ind] == pCount[ind]:
                matches += 1
            elif sCount[ind]== pCount[ind] - 1:
                matches -= 1

            l += 1
        
        if matches == 26:
            res.append(l)
        return res

# Approach 2: O(26N)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        pCount, sCount = [0] * 26, [0] * 26
        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1 
            sCount[ord(s[i]) - ord('a')] += 1 
        
        res = []
        if pCount == sCount:
            res.append(0)
        
        l = 0
        for r in range(len(p), len(s)):
            sCount[ord(s[r]) - ord('a')] += 1 
            sCount[ord(s[l]) - ord('a')] -= 1 

            l += 1
            if sCount == pCount:
                res.append(l)
        
        return res