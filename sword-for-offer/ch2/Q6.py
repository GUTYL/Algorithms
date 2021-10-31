from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """超出时间限制：18/19个通过测试用例"""
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                sum_ = numbers[i] + numbers[j]
                if sum_ == target:
                    return [i, j]

    def twoSum_update1(self, numbers: List[int], target: int) -> List[int]:
        """使用方向相反的双指针优化"""
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i, j]


s = Solution()
print(s.twoSum_update1([-1, 0], -1))
