from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

    def search(self, nums: List[int], target: int) -> bool:
        """二分优化"""
        return target in nums


s = Solution()
print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))
