from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_len, cookie_len = len(g), len(s)
        child, cookie = 0, 0
        while child < g_len and cookie < cookie_len:
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
