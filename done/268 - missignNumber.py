# Approach 1: time: o(n), space: o(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Approach 2: time: o(n), space: o(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = 1

        for i in range(len(nums) + 1):
            if i not in dic:
                return i