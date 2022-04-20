from typing import List
import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        return letters[bisect.bisect_right(letters, target)]

s = Solution()
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="a"))
