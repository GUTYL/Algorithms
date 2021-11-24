from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if nums is None:
            return []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, index, subset, result):
        if index == len(nums):
            return result.append(subset.copy())
        self.helper(nums, index + 1, subset, result)

        subset.append(nums[index])
        self.helper(nums, index + 1, subset, result)
        subset.pop()


s = Solution()
print(s.subsets([1, 2, 3]))
