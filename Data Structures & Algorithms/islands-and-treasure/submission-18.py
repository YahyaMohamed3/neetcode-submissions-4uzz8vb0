class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()
        directions = [[-1, 0] , [1, 0] , [0, 1] , [0, -1]]

        def addCell(r , c):
            if( r not in range(rows) or c not in range(cols) or 
                (r, c) in visited or grid[r][c] == -1):
                return
            
            visited.add((r, c))
            queue.append((r, c))

    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr , dc in directions:
                    addCell(r + dr, c + dc)
            dist+=1 
