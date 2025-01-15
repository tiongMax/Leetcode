# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count2 = bin(num2).count('1')  # Number of 1-bits in num2
        result = 0
        remaining = count2

        # Step 1: Traverse the bits of num1 from most significant to least
        for i in range(31, -1, -1):  # Assuming 32-bit integers
            if num1 & (1 << i):  # Check if the ith bit of num1 is set
                if remaining > 0:  # Keep this bit if we still need 1s
                    result |= (1 << i)
                    remaining -= 1

        # Step 2: If more 1-bits are needed, fill the lowest available bits
        for i in range(32):
            if remaining == 0:
                break
            if not (result & (1 << i)):  # If the ith bit is not set
                result |= (1 << i)
                remaining -= 1

        return result
