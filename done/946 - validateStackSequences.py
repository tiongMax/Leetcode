# https://leetcode.com/problems/validate-stack-sequences/

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
            
        return not stack