class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) \
                or board[r][c] != "O":
                return 

            # Change to other character so that we can change it back easily
            board[r][c] = "T"
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r - 1, c)
            dfs(r + 1, c)

        # Instead of expanding from inside of the board to check for boundary,
        # we start and expand from outside to find for the O inside the board
        # that can be reached by traversing from boundary O
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and \
                    (r in (0, len(board) - 1) or c in (0, len(board[0]) - 1)):
                    dfs(r, c)

        # After that, there is still O in the board, we can safely change it to X
        # as the O are surrounded by X and none of the O can be accessed from the
        # boundary O.
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # We just change the T back to O as required by the question.
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"