from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(i, j, grid))
        return max_area

    def dfs(self, i, j, grid):
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in direct:
            row, col = i + d[0], j + d[1]
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                area += self.dfs(row, col, grid)
        return area


s = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(s.maxAreaOfIsland(grid))
