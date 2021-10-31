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


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
