class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue 
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    rows = (square // 3) * 3 + i 
                    cols = (square % 3) * 3 + j 
                    if board[rows][cols] == ".":
                        continue 
                    if board[rows][cols] in seen:
                        return False
                    seen.add(board[rows][cols])
        return True 

