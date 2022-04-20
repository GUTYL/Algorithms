import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect.bisect(row, target)
            if idx < len(row) and row[idx - 1] == target:
                return True
        return False


print(bisect.bisect([1, 2, 3, 4, 5], 5))
