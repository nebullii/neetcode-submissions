class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        m, n = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            grid[r][c] = 0
            area = 0

            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, bfs(r, c))

        return maxarea



            