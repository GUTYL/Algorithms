import math


class Solution:
    def judgeSquareSum1(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = math.sqrt(c - a * a)
            if b.is_integer():
                return True
            a += 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            sum_ = left * left + right * right
            if sum_ > c:
                right -= 1
            elif sum_ < c:
                left += 1
            else:
                return True
        return False


s = Solution()
print(s.judgeSquareSum(5))
