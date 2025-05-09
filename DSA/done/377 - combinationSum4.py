# https://leetcode.com/problems/combination-sum-iv/

from typing import List 

# Memoization
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}

        def memo(cur):
            if cur > target:
                return 0
            if cur == target:
                return 1 
            if cur in dp:
                return dp[cur]

            count = 0
            for n in nums:
                if cur + n <= target:
                    count += memo(cur + n)

            dp[cur] = count
            return count

        return memo(0)

# Tabulation
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1  
        
        for i in range(target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n] 
        
        return dp[target]