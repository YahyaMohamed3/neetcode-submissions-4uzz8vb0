class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1] , [0 , -1] , [1, 0] , [-1, 0]]
        numIslands = 0

        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] != "1"):
                return
            
            grid[r][c] = "#"

            for dr, dc in directions:
                dfs(dr + r, dc + c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands += 1
                    dfs( r, c )
        return numIslands    