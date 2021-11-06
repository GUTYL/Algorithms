class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1
        for i in t:
            count[ord(i) - ord("a")] -= 1
        if not any(count):
            return True
        return False

    def isAnagram_update(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in s:
            count[ord(i) - ord("a")] += 1
        for i in t:
            if count[ord(i) - ord("a")] == 0:
                return False
            count[ord(i) - ord("a")] -= 1
        return True


s = Solution()
print(s.isAnagram("a", "a"))
