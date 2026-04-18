class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows , cols = len(board) , len(board[0])

        def dfs(r , c , i):
            if i == len(word):
                return True
            # base cases
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i] or board[r][c] =="#"
            ):
                return False
            

            # mark cell as seen
            board[r][c] = "#"

            # recurse over all directions
            directions = [(1, 0), (-1, 0) , (0 , 1) , (0, -1)]
            for dr , dc in directions:
                res = dfs(r + dr, c + dc , i + 1)
                if res:
                    break
            # restore board
            board[r][c] = word[i]
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False




