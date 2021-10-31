from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """超出时间限制：72/94个通过测试用例"""
        i, j = 0, 0
        result = 0
        while i < len(nums):
            j = i
            while j < len(nums):
                tmp = 1
                for a in nums[i:j + 1]:
                    tmp *= a
                if tmp < k:
                    result += 1
                    j += 1
                else:
                    break
            i += 1
        return result


s = Solution()
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
