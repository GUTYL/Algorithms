class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        result = []
        # 进位
        carry = 0
        while i >= 0 or j >= 0:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            # 当前位之和
            sum_ = digit_a + digit_b + carry
            # 是否应该进位
            carry = 1 if sum_ > 1 else 0
            sum_ = sum_ - 2 if carry else sum_
            result.append(str(sum_))
            i -= 1
            j -= 1
        if carry:
            result.append(str(carry))
        return ''.join(reversed(result))


s = Solution()
print(s.addBinary("11", "10"))
print(s.addBinary("1011", "101"))
print(s.addBinary("1010", "1011"))
