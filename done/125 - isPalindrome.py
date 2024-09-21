# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        adjusted = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                adjusted += c.lower() # if c is already in lower case, lower() will just return c
        
        return adjusted[::-1] == adjusted