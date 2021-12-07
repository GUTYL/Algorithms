from common import *


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        originalColor = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
        q = deque([(row, col)])
        visited[row][col] = True
        borders = []
        while q:
            x, y = q.popleft()
            isBorder = False
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                # 判断当前网格块是否为连通分量的边界
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if isBorder:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color

        return grid


url = "https://leetcode-cn.com/problems/coloring-a-border/submissions/"

s = Solution()
print(s.colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2))
