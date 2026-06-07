class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        directions = [[0, 1] , [0, -1] , [1, 0] ,[-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0


        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] != 1):
                return 0
            area = 1
            grid[r][c] = "#"

            for dc, dr in directions:
                area += dfs(r + dr, dc + c)
            return area
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea
