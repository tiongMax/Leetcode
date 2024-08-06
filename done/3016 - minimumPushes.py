# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each character
        char_freq = Counter(word)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
        
        push = 1
        cur_push = 8
        cost = 0
        
        for char, freq in sorted_chars:
            cost += freq * push
            cur_push -= 1
            if cur_push == 0:
                push += 1
                cur_push = 8
        
        return cost