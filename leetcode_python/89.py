import time
from functools import lru_cache, cache
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0, 1]
        for i in range(2, n + 1):
            result += [(1 << (i - 1)) | j for j in result[::-1]]
        return result

    def grayCode1(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        result = self.grayCode1(n - 1)
        result += [(1 << (n - 1)) | j for j in result[::-1]]
        return result

    @cache
    def grayCode2(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        result = self.grayCode2(n - 1)
        result += [(1 << (n - 1)) | j for j in result[::-1]]
        return result

    @lru_cache()
    def grayCode3(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        result = self.grayCode3(n - 1)
        result += [(1 << (n - 1)) | j for j in result[::-1]]
        return result


s = Solution()
t = 16
start = time.time()
s.grayCode(t)
t1 = time.time()

s.grayCode1(t)
t2 = time.time()

s.grayCode2(t)
t3 = time.time()

s.grayCode3(t)
t4 = time.time()
print(t1 - start, t2 - t1, t3 - t2, t4 - t3)
