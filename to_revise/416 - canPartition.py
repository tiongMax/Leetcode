# https://leetcode.com/problems/partition-equal-subset-sum/

from typing import List

## Approach 1: Dp
# 1/ 0 knapsack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        dp = [False] * (target + 1)
        dp[0] = True # It is true that we can have a partition of sum 0 if we have nothing in the partition.
        
        for num in nums:
            temp_dp = dp[:]
            for j in range(num, target + 1):
                temp_dp[j] = dp[j] or dp[j - num]
            dp = temp_dp
        
        return dp[target]


# Neetcode's
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

# Mine
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target % 2 != 0:
            return False
        
        target /= 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            next_dp.add(nums[i])
            for j in dp:
                next_dp.add(j)
                next_dp.add(nums[i] + j)
            if target in next_dp:
                return True
            dp = next_dp

        return False 
    
## Approach 2: Memo (MLE)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        memo = {}
        
        def can_partition(index, current_sum):
            if current_sum == target:
                return True
            if current_sum > target or index >= len(nums):
                return False
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Include the current number in the partition
            include = can_partition(index + 1, current_sum + nums[index])
            # Exclude the current number from the partition
            exclude = can_partition(index + 1, current_sum)
            
            memo[(index, current_sum)] = include or exclude
            return memo[(index, current_sum)]
        
        return can_partition(0, 0)

# Example usage:
# sol = Solution()
# print(sol.canPartition([1, 5, 11, 5]))  # Output: True
# print(sol.canPartition([1, 2, 3, 5]))   # Output: False

    
"""
To check if 2 subsets have equal sum, we can take the sum of the array and divide by 2. So, if the sum
is odd, we will not be able to find them.

If we found a subsequence of sum / 2, we know that the rest of the elements will sum up to sum / 2.

This is a 1 / 0 knapsack problem as we have a target and we can choose to include the elements in the
array or not. So we need a 2d cache. However if the sum of the array is very large, our time and space
complexity will be terrible. Since we just have to check if sum / 2 exists in the cache, we can just use
a set to store all possible subarray sums.
"""