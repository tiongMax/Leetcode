# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Initialize our padded prefix arrays
        prefix_sum = [0] * (n + 1)
        prefix_val = [0] * (n + 1)
        prefix_nonzero = [0] * (n + 1)
        
        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # 2. Build the prefix arrays
        for i in range(n):
            digit = int(s[i])
            
            # Standard prefix sum is always updated
            prefix_sum[i + 1] = prefix_sum[i] + digit
            
            # CRITICAL FIX: Only shift and add to the value if the digit is NOT zero
            if digit != 0:
                prefix_val[i + 1] = (prefix_val[i] * 10 + digit) % MOD
                prefix_nonzero[i + 1] = prefix_nonzero[i] + 1
            else:
                # If it's zero, we just carry forward the previous state 
                # (effectively skipping/removing the 0)
                prefix_val[i + 1] = prefix_val[i]
                prefix_nonzero[i + 1] = prefix_nonzero[i]
            
        results = []
        
        # 3. Process each query
        for l, r in queries:
            L, R = l, r + 1
            
            # Sum of the digits in the range
            current_sum = prefix_sum[R] - prefix_sum[L]
            
            # Find exactly how many non-zero digits are in this specific range
            count = prefix_nonzero[R] - prefix_nonzero[L]
            
            # Isolate the concatenated value and handle modulo for negatives
            current_val = (prefix_val[R] - (prefix_val[L] * pow10[count])) % MOD
            
            # Multiply them together as intended
            ans = (current_sum * current_val) % MOD
            results.append(ans)
            
        return results