from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low_bound = self.low_bound(nums, target)
        high_bound = self.high_bound(nums, target)
        if low_bound == len(nums) or nums[low_bound] != target:
            return [-1, -1]
        return [low_bound, high_bound]

    def low_bound(self, nums: List[int], target: int):
        """查找下界"""
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def high_bound(self, nums: List[int], target: int):
        """查找上界"""
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


s = Solution()
print(s.searchRange(nums=[], target=0))
