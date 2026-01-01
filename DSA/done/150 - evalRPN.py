# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                l, r = stack.pop(), stack.pop()
                stack.append(l + r)
            elif t == '-':
                l, r = stack.pop(), stack.pop()
                stack.append(r - l)
            elif t == '*':
                l, r = stack.pop(), stack.pop()
                stack.append(l * r)
            elif t == '/':
                l, r = stack.pop(), stack.pop()
                stack.append(int(r / l))
            else:
                stack.append(int(t))

        return stack[0]