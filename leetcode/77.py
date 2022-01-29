from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.dfs(1, n, k, [], result)
        return result

    def dfs(self, begin, n, k,  choose, result):
        if len(choose) == k:
            return result.append(choose[:])
        for i in range(begin, n + 1):
            choose.append(i)
            self.dfs(i + 1, n, k, choose, result)
            choose.pop()


s = Solution()
print(s.combine(4, 2))
