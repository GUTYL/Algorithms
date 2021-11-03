from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum = []
        row_len = len(matrix) + 1
        col_len = len(matrix[0]) + 1
        for i in range(row_len):
            tmp = [0] * col_len
            self.sum.append(tmp)
        for row in range(row_len - 1):
            row_sum = 0
            for col in range(col_len - 1):
                row_sum += matrix[row][col]
                self.sum[row + 1][col + 1] = self.sum[row][col + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + \
               self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print(param_1)
