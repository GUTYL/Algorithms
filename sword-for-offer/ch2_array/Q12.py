from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        sum_ = 0
        for i in range(len(nums)):
            if nums[i] + 2 * sum_ == total_sum:
                return i
            sum_ += nums[i]
        return -1


s = Solution()
print(s.pivotIndex([1, -1, 3]))
