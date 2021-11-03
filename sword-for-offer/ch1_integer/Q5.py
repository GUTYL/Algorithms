from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        flags = []
        for word in words:
            tmp = [False] * 26
            for ch in word:
                tmp[ord(ch) - ord('a')] = True
            flags.append(tmp)

        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                k = 0
                for k in range(26):
                    if flags[i][k] and flags[j][k]:
                        break
                if k == 25:
                    prod = len(words[i]) * len(words[j])
                    result = max(result, prod)
        return result

    def maxProduct_update(self, words: List[str]) -> int:
        flags = [0] * len(words)
        for i in range(len(words)):
            for ch in words[i]:
                flags[i] |= 1 << (ord(ch) - ord('a'))

        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if flags[i] & flags[j] == 0:
                    prod = len(words[i]) * len(words[j])
                    result = max(result, prod)
        return result


s = Solution()
print(s.maxProduct_update(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]))
print(s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
