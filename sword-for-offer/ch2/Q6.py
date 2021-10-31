from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) -1):
            for j in range(i + 1, len(numbers)):
                sum_ = numbers[i] + numbers[j]
                if sum_ == target:
                    return [i, j]


s = Solution()
s.twoSum([-1, 0], -1)
