class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0 
        time = 0 
        directions = [[-1 , 0] , [1 ,0] , [0 , -1] , [0 , 1]]


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))


        while queue and fresh > 0:
            length = len(queue)
            for i in range(length):
                r , c = queue.popleft()
                for dr , dc in directions:
                    newR, newC = dr + r, dc + c
                    if (newR in range(rows) and newC in range(cols)
                        and grid[newR][newC] == 1):
                        grid[newR][newC] = 2
                        queue.append((newR, newC))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1