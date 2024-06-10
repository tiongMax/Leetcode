class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set, cur_set = [], []
        self.dfs(0, nums, power_set, cur_set)
        return power_set

    def dfs(self, i, nums, power_set, cur_set):
        if i >= len(nums):
            # Get a new copy to return
            power_set.append(cur_set.copy())
            return 

        # If current element is counted
        cur_set.append(nums[i])
        self.dfs(i + 1, nums, power_set, cur_set)

        # If it is not
        cur_set.pop()
        self.dfs(i + 1, nums, power_set, cur_set)

