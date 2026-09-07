class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        
        return count
