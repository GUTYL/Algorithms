class Solution:
    def process1(self, dividend: int, divisor: int):
        """dividend > 0, divisor > 0"""
        result = -1 if divisor < 0 else 1
        tmp = 0
        while True:
            if tmp < dividend:
                tmp += divisor
                result += 1
            elif tmp >= dividend:
                return result

    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 1:
            return 1
        if divisor == -1:
            return -dividend
        if dividend < divisor:
            return 0
        if dividend > 0 and divisor > 0:
            return self.process1(-dividend, -divisor)
        divmod(10, -3)
        return self.process2(dividend, divisor)


# s = Solution()
# print(s.divide(10, 3))
# print(s.divide(-1, 1))
# print(s.divide(1, 1))
print(-2**31)
print(10/-3)