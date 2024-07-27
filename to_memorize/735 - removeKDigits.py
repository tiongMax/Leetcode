# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # stack[-1] must be strictly greater than digit
            # The previous number is same as me and the next number is
            # greater and k = 1, if current number is popped out, the final result will
            # have a greater value. If it is not popped out, the next number will be 
            # popped out. For example, num = 112 and k = 1
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if len(stack) == 1 and stack[0] == 0:
            return "0"

        # Remove any remaining digits from the end if k > 0
        stack = stack[:-k] if k > 0 else stack
        
        # Convert stack to string
        result = ''.join(stack)
        
        # Manually strip leading zeros
        i = 0
        while i < len(result) and result[i] == '0':
            i += 1
        
        result = result[i:]
        return result if result else '0'

