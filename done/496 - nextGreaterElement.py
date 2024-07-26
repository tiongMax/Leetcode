# https://leetcode.com/problems/next-greater-element-i/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            if not stack:
                hm[nums2[i]] = -1
            else:
                while stack and stack[-1] <= nums2[i]:
                    stack.pop()

                hm[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        res = []
        for v in nums1:
            res.append(hm[v])

        return res


            
