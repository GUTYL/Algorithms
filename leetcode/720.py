from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set(words)
        result = ''
        for word in words_set:
            time = 0
            for i in range(len(word)):
                if word[:i + 1] not in words_set:
                    continue
                time += 1
            if time == len(word) and len(word) >= len(result):
                if not (len(word) == len(result) and word > result):
                    result = word
        return result


s = Solution()
print(s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
