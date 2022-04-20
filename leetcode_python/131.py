from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        ans = []

        def dfs(index):
            if index == n:
                result.append(ans[:])
            for i in range(index, n + 1):
                tmp = s[index:i + 1]
                if tmp == tmp[::-1]:
                    ans.append(s[index: i + 1])
                    dfs(i + 1)
                    ans.pop()

        dfs(0)
        return result


s = Solution()
print(s.partition('aab'))
