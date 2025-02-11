# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= part_len and stack[-part_len:] == list(part):
                for _ in range(part_len):
                    stack.pop()
        return "".join(stack)
