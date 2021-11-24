from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        result = []
        self.helper(nums, k, 0, [], result)
        return result

    def helper(self, nums, deepth, index, subset, result):
        if len(subset) == deepth:
            return result.append(subset.copy())
        if index == len(nums):
            return
        self.helper(nums, deepth, index + 1, subset, result)
        subset.append(nums[index])
        self.helper(nums, deepth, index + 1, subset, result)
        subset.pop()

    def combine_update(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []
        self.helper_update(n, k, 1, combination, result)
        return result

    def helper_update(self, n, k, i, combination, result):
        if len(combination) == k:
            return result.append(combination.copy())
        if i <= n:
            self.helper_update(n, k, i + 1, combination, result)
            combination.append(i)
            self.helper_update(n, k, i + 1, combination, result)
            combination.pop()


s = Solution()
print(s.combine(4, 2))
