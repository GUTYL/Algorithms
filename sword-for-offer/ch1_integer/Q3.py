from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            j = i
            while j > 0:
                # 使用j & (j - 1) 移除最右边的1
                j = j & (j - 1)
                result[i] += 1
        return result

    def countBits_update1(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i & (i - 1)] + 1
        return result

    def countBits_update2(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result


s = Solution()
print(s.countBits_update2(4))
print(s.countBits_update2(5))
