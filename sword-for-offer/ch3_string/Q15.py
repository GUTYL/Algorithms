from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """时间超限，34/60个通过测试用例"""
        if len(s) < len(p):
            return []
        p_ch = [0] * 26
        result = []
        for i in p:
            p_ch[ord(i) - ord('a')] += 1
        for i in range(len(s) - len(p) + 1):
            sub_ch = [0] * 26
            for j in s[i: i + len(p)]:
                sub_ch[ord(j) - ord('a')] += 1
            if sub_ch == p_ch:
                result.append(i)
        return result

    def findAnagrams_update(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        counts = [0] * 26
        result = []
        for i in p:
            counts[ord(i) - ord('a')] += 1
        for i in s[:len(p)]:
            counts[ord(i) - ord('a')] -= 1
        if not any(counts):
            result.append(0)

        for i in range(len(p), len(s)):
            counts[ord(s[i]) - ord('a')] -= 1
            counts[ord(s[i - len(p)]) - ord('a')] += 1
            if not any(counts):
                result.append(i - len(p) + 1)
        return result
