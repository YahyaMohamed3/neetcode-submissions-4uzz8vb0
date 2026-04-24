class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        directions = [[-1, 0] , [1, 0] , [0 , 1] , [0, -1]]

        def dfs(r , c):
            if(r not in range(rows) or c not in range(cols) or grid[r][c] != 1):
                return 0
            grid[r][c] = "#"
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr , c + dc)
            return area 
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea