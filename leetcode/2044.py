from typing import List


class Solution:
    def __init__(self):
        self.max_val = 0
        self.count = 0

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        for i in nums:
            self.max_val |= i
        self.backtrack(0, 0, nums)
        return self.count

    def backtrack(self, cur, index, nums):
        if cur == self.max_val:
            self.count += 1
        for i in range(index, len(nums)):
            tmp = cur
            cur |= nums[i]
            self.backtrack(cur, i + 1, nums)
            cur = tmp


s = Solution()
print(s.countMaxOrSubsets([3, 1]))
