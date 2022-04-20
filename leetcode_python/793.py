class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 1
        divmod(9, 4)
        return n * self.trailingZeroes(n - 1)



s = Solution()
print(s.trailingZeroes(30))
