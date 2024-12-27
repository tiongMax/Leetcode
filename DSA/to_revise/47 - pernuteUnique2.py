# Approach 1: faster
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Create a hashmap for the count of each num in nums
        hm = Counter(nums)
        res = []
        cur_perm = []

        def backTrack():
            if len(cur_perm) == len(nums):
                res.append(cur_perm.copy())
                return
            
            # When we dive into the tree, we deduct the occurrence of the num
            for n in hm:
                # If there is no occurence of the num, we dont add to cur_perm
                if hm[n] > 0:
                    cur_perm.append(n)
                    hm[n] -= 1
                    backTrack()

                    hm[n] += 1
                    cur_perm.pop()

        backTrack()
        return res
                
# Approach 2:
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            next_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    if p_copy not in next_perms:
                        next_perms.append(p_copy)
            perms = next_perms

        return perms