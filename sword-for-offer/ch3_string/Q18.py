import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """过滤掉非字母数数字的字符，判断是否与逆序相同
        回文字符串逆序后与原字符串相同"""
        chars = string.ascii_letters + string.digits
        new_str = ''
        for i in s:
            if i in chars:
                new_str += i.lower()
        return new_str == new_str[::-1]

    def isPalindrome_update(self, s: str) -> bool:
        """使用双指针实现"""
        start, end = 0, len(s) - 1
        while start <= end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
        return True


s = Solution()
print(s.isPalindrome("1:A man, a plan, a canal: Panama1"))
