import sys
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        right, left = 0, 0
        min_right, min_left = 0, 0
        char_to_count = defaultdict(int)
        for i in t:
            char_to_count[i] += 1
        count = len(char_to_count.items())
        min_len = sys.maxsize
        while right < len(s) or (count == 0 and right == len(s)):
            if count > 0:
                right_ch = s[right]
                if right_ch in char_to_count.keys():
                    char_to_count[right_ch] -= 1
                    if char_to_count[right_ch] == 0:
                        count -= 1
                right += 1
            else:
                if right - left < min_len:
                    min_len = right - left
                    min_right = right
                    min_left = left
                left_ch = s[left]
                if left_ch in char_to_count.keys():
                    char_to_count[left_ch] += 1
                    if char_to_count.get(left_ch) == 1:
                        count += 1
                left += 1
        if min_len < sys.maxsize:
            return s[min_left: min_right]

        return ""


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
