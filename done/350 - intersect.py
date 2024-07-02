# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        count1 = Counter(nums1)
        res = []
        
        for num in nums2:
            # If num is not in count1, it will return 0 instead of throwing
            # key error if we use Counter. 
            if count1[num] > 0:
                res.append(num)
                count1[num] -= 1
        
        return res
