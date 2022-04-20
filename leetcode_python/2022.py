from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i: i + n] for i in range(0, len(original), n)]
s = Solution()
print(s.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
