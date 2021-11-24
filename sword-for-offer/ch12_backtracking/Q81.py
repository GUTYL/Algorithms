from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        self.helper(candidates, target, 0, combination, result)
        return result

    def helper(self, candidates, target, index, combination, result):
        if target == 0:
            return result.append(combination.copy())
        if target > 0 and index < len(candidates):
            self.helper(candidates, target, index + 1, combination, result)
            combination.append(candidates[index])
            self.helper(candidates, target - candidates[index], index, combination, result)
            combination.pop()

    def combinationSum_update(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        self.helper_update(candidates, target, 0, combination, result)
        return result

    def helper_update(self, candidates, target, index, combination, result):
        if target == 0:
            return result.append(combination.copy())
        if target < 0:
            return
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.helper_update(candidates, target - candidates[i], i, combination, result)
            combination.pop()


s = Solution()
print(s.combinationSum_update([2, 3, 5], 8))
