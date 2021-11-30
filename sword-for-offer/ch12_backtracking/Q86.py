from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        sub = []
        self.helper(0, s, sub, result)
        return result

    def helper(self, start, s, sub, result):
        if start == len(s):
            result.append(sub.copy())
        for i in range(start, len(s)):
            tmp = s[start: i + 1]
            if tmp == tmp[::-1]:
                sub.append(tmp)
                self.helper(i + 1, s, sub, result)
                sub.pop()
