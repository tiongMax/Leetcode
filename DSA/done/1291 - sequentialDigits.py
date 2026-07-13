# https://leetcode.com/problems/sequential-digits

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_len, max_len = len(str(low)), len(str(high))
        mas_str = "123456789"
        res = []
        
        for i in range(min_len, max_len + 1):
            l = 0
            # len(mas_str) + 1 ensures the right pointer 'r' can reach index 9 for slicing
            for r in range(i, len(mas_str) + 1):
                seq_dig = int(mas_str[l:r])
                
                if low <= seq_dig <= high: 
                    res.append(seq_dig)
                
                # Optional Optimization: if it's already too big, stop checking this length
                if seq_dig > high:
                    break
                    
                l += 1
        
        return res