# https://leetcode.com/problems/partition-array-for-maximum-sum/

from typing import List

# Approach 1: Dp
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_sum = maxi = size = 0
            for j in range(i, min(n, i + k)):
                size += 1
                maxi = max(maxi, arr[j])
                cur_sum = (maxi * size) + dp[j + 1]
                max_sum = max(max_sum, cur_sum)
            dp[i] = max_sum

        return dp[0]

# Approach 2: Memo
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}
        
        def memo(i): 
            if i == len(arr):
                return 0
            if i in dp:
                return dp[i]

            max_sum = maxi = size = 0
            for j in range(i, min(len(arr), i + k)):
                size += 1
                maxi = max(maxi, arr[j])
                cur_sum = (maxi * size) + memo(j + 1)
                max_sum = max(max_sum, cur_sum)
            
            dp[i] = max_sum
            return max_sum
        return memo(0)