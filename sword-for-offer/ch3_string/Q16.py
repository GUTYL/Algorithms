from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, right = 0, 0
        max_len = 0
        ch_to_num = defaultdict(int)
        while right < len(s):
            max_len = max(max_len, right - left)
            ch_to_num[s[right]] += 1
            while ch_to_num[s[right]] > 1:
                ch_to_num[s[left]] -= 1
                left += 1
            right += 1
        max_len = max(max_len, right - left)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring(" "))
