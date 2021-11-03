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

    def numSubarrayProductLessThanK_update1(self, nums: List[int], k: int) -> int:
        """使用方向相同的双指针更新
        """
        product = 1
        left = 0
        result = 0
        for right, num in enumerate(nums):
            product *= num
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            if left <= right:
                result += right - left + 1
        return result


s = Solution()
print(s.numSubarrayProductLessThanK([1, 2, 3], 0))
