from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_sums = [0] * 32
        for num in nums:
            for i in range(32):
                # (num >> (31 - i)) & 1，用来得到整数num的二进制形式中从左数起第i个数位
                bit_sums[i] += (num >> (31 - i)) & 1
        result = 0
        for i in range(1, 32):
            result = (result << 1) + bit_sums[i] % 3
        # python 整数为无符号，需要对首位为1(符号位标识为负数）的情况特殊处理
        if bit_sums[0] % 3 == 1:
            result -= 1 << 31
        return result


s = Solution()
print(s.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
