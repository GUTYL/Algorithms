import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """超出时间限制：18/19个通过测试用例"""
        if sum(nums) < target:
            return 0
        if target in nums:
            return 1
        for i in range(1, len(nums) + 1):
            start = 0
            while start <= (len(nums) - i):
                tmp = sum(nums[start: start + i])
                if tmp >= target:
                    return i
                start += 1

    def minSubArrayLen_update(self, target: int, nums: List[int]) -> int:
        """方向相同的双指针优化
        """
        left = 0
        sum_ = 0
        min_len = sys.maxsize
        for right in range(len(nums)):
            sum_ += nums[right]
            while left <= right and sum_ >= target:
                min_len = min(min_len, right - left + 1)
                sum_ -= nums[left]
                left += 1

        return 0 if min_len == sys.maxsize else min_len


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
