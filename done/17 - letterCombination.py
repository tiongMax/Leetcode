from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], 
                5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'], 
                7 : ['p', 'q', 'r', 's'], 8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z']}
        res = []

        def helper(i, cur_str):   
            if i >= len(digits):
                res.append(cur_str)
                return

            for k in dic[int(digits[i])]:
                helper(i + 1, cur_str + k)
                
        helper(0, "")
        return res