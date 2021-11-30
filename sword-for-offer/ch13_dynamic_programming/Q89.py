from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """纯递归，超出时间限制 48/68个通过测试用例"""
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(n - 1, nums), self.helper(n - 2, nums))

    def helper(self, n, nums):
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0], nums[1])
        return max(self.helper(n - 1, nums), self.helper(n - 2, nums) + nums[n])

    def rob_update1(self, nums: List[int]) -> int:
        """递归+dp数组剪枝"""
        lens = len(nums)
        if lens < 2:
            return nums[0]
        dp = [-1] * lens
        self.helper_update1(lens - 1, nums, dp)
        return dp[lens - 1]

    def helper_update1(self, n, nums, dp):
        if n == 0:
            dp[0] = nums[0]
        elif n == 1:
            dp[1] = max(nums[0], nums[1])
        elif dp[n] == -1:
            self.helper_update1(n - 1, nums, dp)
            self.helper_update1(n - 2, nums, dp)
            dp[n] = max(dp[n - 1], dp[n - 2] + nums[n])

    def rob_update2(self, nums: List[int]) -> int:
        """迭代+dp数组"""
        lens = len(nums)
        if lens < 2:
            return nums[0]
        dp = [-1] * lens
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, lens):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[lens - 1]

    def rob(self, nums: List[int]) -> int:
        """迭代+dp数组空间优化"""
        lens = len(nums)
        if lens < 2:
            return nums[0]
        dp = [-1] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, lens):
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
        return dp[(lens - 1) % 2]
