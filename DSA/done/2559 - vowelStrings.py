# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] 
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])
        
        return result
