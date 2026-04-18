class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or board[r][c] == "#"):
                return False
            
            board[r][c] = "#"
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            res = False
            for dr, dc in directions:
                res = dfs(r + dr, c + dc, i + 1)
                if res:
                    break
            board[r][c] = word[i]  # restore
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False