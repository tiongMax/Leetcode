# https://leetcode.com/problems/word-break/

from typing import List

# Approach 1: Memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def canBreak(start: int) -> bool:
            # If we reach the end of the string, return True
            if start == len(s):
                return True
            
            # If we have already computed the result for this substring, return it
            if start in memo:
                return memo[start]
            
            # Try every word in the dictionary
            for word in wordDict:
                end = start + len(word)
                # Check if the word matches the substring starting at index start
                if end <= len(s) and s[start:end] == word:
                    # If we can break the remaining substring, return True
                    if canBreak(end):
                        memo[start] = True
                        return True
            
            # If no word matches, store False in memo and return False
            memo[start] = False
            return False
        
        # Start the recursion from the beginning of the string
        return canBreak(0)

# Approach 2: Dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                j = len(word)
                # If the length and the word matches the substring, we can just 
                # assign it with the result of the next substring (can we break the
                # next substring starting from here if we manage to reach here).
                if i + j <= len(s) and s[i : i + j] == word:
                    dp[i] = dp[i + j]
                # One of the word matches the curr substring, so we can stop early.
                if dp[i]:
                    break
                
        return dp[0]


