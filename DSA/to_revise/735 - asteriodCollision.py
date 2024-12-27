# https://leetcode.com/problems/asteroid-collision/

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # if top of stack and current a are both > 0
            if a > 0 and stack and stack[-1] > 0:
                stack.append(a)
                continue
            
            # if stack[-1] > 0 and current a is < 0 and stack[-1] < abs(current a)
            while stack and a < 0 and stack[-1] > 0 and abs(a) > stack[-1]:
                stack.pop()

            # if top of stack == abs(current a)
            if stack and stack[-1] == abs(a):
                stack.pop()
                continue
                
            # if the stack is empty or stack[-1] and current a are both < 0
            elif (not stack) or stack[-1] < 0:
                stack.append(a)

        return stack

            