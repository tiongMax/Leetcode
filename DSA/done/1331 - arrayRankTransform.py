# https://leetcode.com/problems/rank-transform-of-an-array/description

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []
            
        # Pair each element with its original index and sort by the element's value
        sorted_pairs = sorted([(val, i) for i, val in enumerate(arr)], key=lambda x: x[0])
        
        # Initialize the result array with zeros
        res = [0] * len(arr)
        
        # Start ranking at 1
        rank = 1
        
        # Assign the rank for the smallest element
        res[sorted_pairs[0][1]] = rank
        
        # Iterate through the rest of the sorted pairs
        for i in range(1, len(sorted_pairs)):
            current_val, original_idx = sorted_pairs[i]
            prev_val = sorted_pairs[i-1][0]
            
            # Increment rank only if the current value is strictly greater
            if current_val > prev_val:
                rank += 1
                
            # Place the rank at the element's original position
            res[original_idx] = rank
            
        return res