from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], nums, result)
        return result

    def backtrack(self, chiose, nums, result):
        if len(chiose) == len(nums):
            return result.append(chiose.copy())
        for i in nums:
            if i not in chiose:
                chiose.append(i)
                self.backtrack(chiose, nums, result)
                chiose.pop()

    def permute_update1(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtrack_update1(used, [], nums, result)
        return result

    def backtrack_update1(self, used, chiose, nums, result):
        if len(chiose) == len(nums):
            return result.append(chiose.copy())
        for index, val in enumerate(nums):
            if not used[index]:
                chiose.append(val)
                used[index] = True
                self.backtrack_update1(used, chiose, nums, result)
                chiose.pop()
                used[index] = False
