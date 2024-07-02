# https://leetcode.com/problems/coin-change/

from typing import List

# Approach 1: Dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value greater than the possible maximum number of coins
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Iterate over all amounts from 1 to amount
        for i in range(1, amount + 1):
            # Check each coin to find the minimum number of coins required
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]

# Approach 2: Memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def helper(rem: int) -> int:
            # Base cases
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            
            # Recursive case: try every coin and find the minimum
            min_coins = float('inf')
            for coin in coins:
                result = helper(rem - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)
            
            memo[rem] = min_coins
            return memo[rem]
        
        result = helper(amount)
        return -1 if result == float('inf') else result

