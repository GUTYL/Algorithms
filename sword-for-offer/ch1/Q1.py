class Solution:
    def divide_fail(self, a: int, b: int) -> int:
        """超时"""
        # 溢出情况 -2**31/-1
        if a == -2 ** 31 and b == -1:
            return 2 ** 31 - 1
        # 返回是否为负
        negative = 2
        if a < 0:
            a = -a
            negative -= 1
        if b < 0:
            b = -b
            negative -= 1
        result = 0
        while a >= b:
            if a >= b:
                result += 1
            a -= b

        if negative == 1:
            result = -result
        return result

    def divide(self, a: int, b: int) -> int:
        # 溢出情况 -2**31/-1
        if a == -2 ** 31 and b == -1:
            return 2 ** 31 - 1
        # 返回是否为负，异或运算
        sign = 1 if (a > 0) ^ (b > 0) else -1
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        result = 0
        while a >= b:
            value = b
            quotient = 1
            while a >= value + value:
                quotient += quotient
                value += value
            result += quotient
            a -= value
        if sign == -1:
            result = -result
        return result


s = Solution()
print(s.divide(15, 2))
print(s.divide(7, -3))
print(s.divide(10, 10))
print(s.divide(10, -10))
