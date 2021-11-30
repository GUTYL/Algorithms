from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        """递归+dp数组剪枝"""
        lens = len(nums)
        if lens == 1:
            return nums[0]
        if lens == 2:
            return max(nums[0], nums[1])
        result1 = self.helper(nums, 0, lens - 2)
        result2 = self.helper(nums, 1, lens - 1)
        return max(result1, result2)

    def helper(self, nums, start, end):
        dp = [-1] * 2
        dp[0] = nums[start]
        if start < end:
            dp[1] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            j = i - start
            dp[j % 2] = max(dp[(j - 1) % 2], dp[(j - 2) % 2] + nums[i])
        return dp[(end - start) % 2]


s = Solution()
print(s.rob([0]))
