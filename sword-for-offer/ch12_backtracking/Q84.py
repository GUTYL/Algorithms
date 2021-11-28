from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False] * len(nums)
        self.backtrack(used, [], nums, result)
        return result

    def backtrack(self, used, chiose, nums, result):
        if len(chiose) == len(nums):
            result.append(chiose.copy())
            return
        for index, val in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1] and not used[index - 1]:
                continue
            if not used[index]:
                chiose.append(val)
                used[index] = True
                self.backtrack(used, chiose, nums, result)
                chiose.pop()
                used[index] = False
