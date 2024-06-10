class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        col = set()
        neg_diag = set() # r - c
        pos_diag = set() # r + c

        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Note that the sum of each coordinate in the same positive gradient 
                # diagonal has the same value.
                # Vice versa.
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                board[r][c] = 'Q'
                backTrack(r + 1)

                col.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                board[r][c] = '.'

        backTrack(0)
        return res