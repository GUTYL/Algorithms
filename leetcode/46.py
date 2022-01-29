from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, choose, result):
        if len(choose) == len(nums):
            result.append(choose[:])
            return
        for i in nums:
            if i not in choose:
                choose.append(i)
                self.dfs(nums, choose, result)
                choose.pop()


s = Solution()
print(s.permute([1, 2, 3]))
