from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lens = len(cost)
        return min(self.helper(lens - 1, cost), self.helper(lens - 2, cost))

    def helper(self, n, cost):
        """超时，259/283个通过测试用例"""
        if n < 2:
            return cost[n]
        return min(self.helper(n - 1, cost), self.helper(n - 2, cost)) + cost[n]

    def minCostClimbingStairs_update1(self, cost: List[int]) -> int:
        lens = len(cost)
        dp = [-1] * lens
        dp[0] = cost[0]
        dp[1] = cost[1]
        self.helper_update1(lens - 1, cost, dp)
        return min(dp[lens - 1], dp[lens - 2])

    def helper_update1(self, n, cost, dp):
        if dp[n] == -1:
            self.helper_update1(n - 2, cost, dp)
            self.helper_update1(n - 1, cost, dp)
            dp[n] = min(dp[n - 1], dp[n - 2]) + cost[n]

    def minCostClimbingStairs_update2(self, cost: List[int]) -> int:
        lens = len(cost)
        dp = [-1] * lens
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, lens):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        return min(dp[lens - 1], dp[lens - 2])

    def minCostClimbingStairs_update3(self, cost: List[int]) -> int:
        lens = len(cost)
        dp = [-1] * 2
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, lens):
            dp[i % 2] = min(dp[(i - 2) % 2], dp[(i - 1) % 2]) + cost[i]
        return min(dp[(lens - 1) % 2], dp[(lens - 2) % 2])


s = Solution()
print(s.minCostClimbingStairs_update3([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
