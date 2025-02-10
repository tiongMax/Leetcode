# https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit() and stack:
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)