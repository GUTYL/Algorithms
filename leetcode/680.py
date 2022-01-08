class Solution:
    def validPalindrome1(self, s: str) -> bool:
        """时间超限"""
        for i in range(len(s)):
            sub = s[:i] + s[i + 1:]
            if sub == sub[::-1]:
                return True
        return False

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        check = lambda i, j: s[i:j] == s[i:j][::-1]
        while left < right:
            if s[left] != s[right]:
                if check(left + 1, right + 1) or check(left, right):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True


s = Solution()
print(s.validPalindrome("adca"))
