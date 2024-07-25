# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for s1 and the initial window of s2
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Populate the frequency array for s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Initialize the first window in s2
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        
        # Check the initial window
        if s1_count == window_count:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Include the new character in the window
            window_count[ord(s2[i]) - ord('a')] += 1
            # Exclude the old character from the window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Check if the current window matches the frequency of s1
            if s1_count == window_count:
                return True
        
        return False
