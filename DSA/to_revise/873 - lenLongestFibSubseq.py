# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_map = {n: i for i, n in enumerate(arr)}  # map of elements to their indices
        res = 0
        dp = [[0] * len(arr) for _ in range(len(arr))]  # DP table to store lengths

        for i in reversed(range(len(arr) - 1)):
            for j in reversed(range(i + 1, len(arr))):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2  # Fibonacci sequence needs at least two elements

                if nxt in arr_map:  # If the next number exists in the sequence
                    length = 1 + dp[j][arr_map[nxt]]  # Calculate the length
                    res = max(res, length)  # Track the maximum length

                dp[i][j] = length  # Update DP table

        return res
