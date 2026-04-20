class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addCell(r , c):
            if r < 0 or c < 0 or r == rows or c == cols \
            or (r , c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r ,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = dist
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r , c + 1)
                addCell(r, c - 1)
            dist += 1
           

# Multi-source BFS from all gates (0s) simultaneously
# Each cell gets updated with its distance to nearest gate
# -1 = wall (skip), 0 = gate (source), INF = empty room
# BFS guarantees shortest distance layer by layer