class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if not dividend:
            return 0
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        flag = 0 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        for n in range(31, -1, -1):
            if (dividend >> n) >= divisor:
                result += 1 << n
                dividend -= divisor << n
                continue
        return result if flag else -result


s = Solution()
print(s.divide(10, 3))
print(s.divide(-1, 1))
print(s.divide(1, 1))
print(s.divide(-2, 31))
print(s.divide(10, -3))
