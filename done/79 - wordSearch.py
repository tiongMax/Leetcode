class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backTrack(i, x, y):
            if i == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y] or board[x][y] != word[i]:
                return False

            visited[x][y] = True
            found = backTrack(i + 1, x + 1, y) or backTrack(i + 1, x - 1, y) or \
                    backTrack(i + 1, x, y + 1) or backTrack(i + 1, x, y - 1)
            visited[x][y] = False
            
            return found

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backTrack(0, r, c):
                    return True

        return False
