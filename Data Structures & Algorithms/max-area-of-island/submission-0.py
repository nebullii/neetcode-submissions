class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            result = 1

            while q:
                x, y = q.popleft()
                for dr, dc in directions:
                    m, n = dr + x, dc + y
                    if (0 <= m < rows and
                        0 <= n < cols and
                        grid[m][n] == 1
                    ):
                        grid[m][n] = 0 
                        q.append((m, n))
                        result += 1
            return result

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        
        return area
