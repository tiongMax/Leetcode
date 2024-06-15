class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pos_diag = set()
        neg_diag = set()
        res = 0

        def backTrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in col or r + c in pos_diag or r - c in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                backTrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backTrack(0)
        return res
