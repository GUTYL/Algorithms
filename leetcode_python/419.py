from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        nums_ship = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and board[i][j] == 'X':
                    visited[i][j] = 1
                    self.find_ship(i, j, m, n, visited, board)
                    nums_ship += 1
        return nums_ship

    def find_ship(self, col, row, m, n, visited, board):
        # 水平放置
        for i in range(row + 1, n):
            if board[col][i] != 'X':
                break
            visited[col][i] = 1
        # 垂直放置
        for i in range(col + 1, m):
            if board[i][row] != 'X':
                break
            visited[i][row] = 1




s = Solution()
board = [["X",".","X"],["X",".","X"]]
print(s.countBattleships(board))
