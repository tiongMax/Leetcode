# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        hm = Counter(t)
        required = len(hm)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        min_len = float('inf')
        min_window = (0, 0)
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in hm and window_counts[character] == hm[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)
                
                window_counts[character] -= 1
                # Check if the char removed is in hm and the num of character of t
                # is still satisfied (some char might have extra occurence, so
                # deducting one from it will satisfy the constrain)
                if character in hm and window_counts[character] < hm[character]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if min_len == float('inf') else s[min_window[0]:min_window[1] + 1]
