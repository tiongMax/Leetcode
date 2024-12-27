class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur_sub = []
        def backTrack(i):
            if i == len(s):
                res.append(cur_sub.copy())
                return

            # Check if the substring from i to j inclusive that is palindromic then
            # recursively call the backTrack function with s starts from j + 1.
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                if sub == sub[::-1]:
                    cur_sub.append(sub)
                    backTrack(j + 1)
                    cur_sub.pop()

        backTrack(0)
        return res
